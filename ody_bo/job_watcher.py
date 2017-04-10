import os
import shutil
import importlib.util
import time
import sys
import argparse


def check_new(calc_dir, bo_job_dir, job_id):
    job_pre = 'job_{:d}'.format(job_id)
    new_dir = os.path.join(bo_job_dir, job_pre)
    if os.path.isdir(new_dir):
        time.sleep(5)
        inbox_dir = os.path.join(calc_dir, 'inbox')
        print('mv job_{:d}'.format(job_id), end='')
        shutil.move(new_dir, inbox_dir)
    return


def check_result(calc_dir, bo_job_dir, job_id):
    # check if result exists
    dst_file = os.path.join(bo_job_dir, 'results.out')
    if not os.path.exists(dst_file):
        # check if the folder is ready
        done_dir = os.path.join(calc_dir, 'completed',
                                'job_{:d}'.format(job_id))
        if bo_utils.is_ready(done_dir):
            src_file = os.path.join(done_dir, 'results.out')
            shutil.copy(src_file, dst_file)
            copy_file = os.path.join(done_dir, 'results_parsed.out')
            shutil.move(src_file, copy_file)
            print('mv result_{:d}'.format(job_id), end='')
    return


def main(calc_dir, bo_dir):
    bo_job_dir = os.path.join(bo_dir, 'jobs')
    count = 0
    while True:
        job_id = bo_utils.read_iteration(bo_job_dir)
        # check if there is a new job_calcution ready
        check_new(calc_dir, bo_job_dir, job_id)
        # check if there is a new result
        check_result(calc_dir, bo_job_dir, job_id)
        # time looping
        pend = '\n' if count % 20 == 19 else ''
        print('.', end=pend)
        sys.stdout.flush()
        count += 1
        time.sleep(30)
    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='watch jobs from a job manager')
    parser.add_argument('spearmint_dir', type=str,
                        help='a file path containing a spearmint experiment')
    parser.add_argument('job_dir', type=str,
                        help='a file path where to transfer and monitor the jobs')
    global bo_utils
    args = parser.parse_args()
    # load module of utilities
    spec = importlib.util.spec_from_file_location(
        "bo_utils", "{}/bo_utils.py".format(args.spearmint_dir))
    bo_utils = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bo_utils)

    main(calc_dir=args.job_dir,
         bo_dir=args.spearmint_dir)
