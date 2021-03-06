from __future__ import print_function
import os
import shutil
import time
import sys
import argparse
import imp


def check_new(calc_dir, bo_job_dir, job_id):
    job_pre = '{:d}'.format(job_id)
    new_dir = os.path.join(bo_job_dir, job_pre)
    if os.path.isdir(new_dir):
        time.sleep(5)
        inbox_dir = os.path.join(calc_dir, 'inbox')
        print('\n\t---> moved new job {:d}'.format(job_id))
        shutil.move(new_dir, inbox_dir)
    return


def check_result(calc_dir, bo_job_dir, job_id):
    # check if result exists
    done_dir = os.path.join(calc_dir, 'completed',
                            '{:d}'.format(job_id))
    # check if job is done
    if bo_utils.is_ready(job_id, done_dir):
        done_src = os.path.join(done_dir, '{:d}.done'.format(job_id))
        done_dst = os.path.join(bo_job_dir, '{:d}.done'.format(job_id))
        shutil.copy(done_src, done_dst)
        # check if reult file exists
        src_file = os.path.join(done_dir, 'results.out')
        if os.path.exists(src_file):
            dst_file = os.path.join(bo_job_dir, 'results.out')
            shutil.copy(src_file, dst_file)
            print('\n\t---> copied result #{:d}'.format(job_id))
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
    args = parser.parse_args()
    # load module of utilities
    global bo_utils
    util_path = os.path.join(args.spearmint_dir, "bo_utils.py")
    bo_utils = imp.load_source('bo_utils', util_path)

    main(calc_dir=args.job_dir,
         bo_dir=args.spearmint_dir)
