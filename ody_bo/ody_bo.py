from __future__ import print_function
import os
from ody_utils import create_job, parse_job, not_ready
import time

INPUT_DIR = os.path.join(os.getcwd(), 'Jobs/inbox')
OUTPUT_DIR = os.path.join(os.getcwd(), 'Jobs/completed')


def main(job_id, params):
    print('Job #%d' % job_id)
    print(params)
    create_job(job_id, params, INPUT_DIR)

    while not_ready(job_id, OUTPUT_DIR):
        time.sleep(5)

    result = parse_job(job_id, OUTPUT_DIR)
    print('Result = {:f}'.format(result))
    return result

if __name__ == "__main__":
    print('testing')
