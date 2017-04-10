import os
import shutil
import importlib.util
import time
import sys

# local directory where odyssey was mounted
CALC_DIR = '/home/beangoben/projects/test/jobs'
# local directory for docker/speamint experiment
BO_DIR = '/home/beangoben/projects/spearmint_docker/ody_bo'
bo_job_dir = os.path.join(BO_DIR, 'jobs')
# load module of utilities
spec = importlib.util.spec_from_file_location(
    "bo_utils", "{}/bo_utils.py".format(BO_DIR))
bo_utils = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bo_utils)


def check_new(job_id):
    job_pre = 'job_{:d}'.format(job_id)
    new_dir = os.path.join(bo_job_dir, job_pre)
    if os.path.isdir(new_dir):
        time.sleep(5)
        inbox_dir = os.path.join(CALC_DIR, 'inbox')
        print('mv job_{:d}'.format(job_id), end='')
        shutil.move(new_dir, inbox_dir)
    return


def check_result(job_id):
    # check if result exists
    dst_file = os.path.join(bo_job_dir, 'results.out')
    if not os.path.exists(dst_file):
        # check if the folder is ready
        done_dir = os.path.join(CALC_DIR, 'completed',
                                'job_{:d}'.format(job_id))
        if bo_utils.is_ready(done_dir):
            src_file = os.path.join(done_dir, 'results.out')
            shutil.copy(src_file, dst_file)
            print('mv result_{:d}'.format(job_id), end='')
    return


def main():
    count = 0
    while True:
        job_id = bo_utils.read_iteration(bo_job_dir)
        # check if there is a new job_calcution ready
        check_new(job_id)
        # check if there is a new result
        check_result(job_id)
        # time looping
        pend = '\n' if count % 20 == 19 else ''
        print('.', end=pend)
        sys.stdout.flush()
        count += 1
        time.sleep(5)
    return

if __name__ == "__main__":
    main()
