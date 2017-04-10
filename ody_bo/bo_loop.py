from __future__ import print_function
import os
from bo_utils import create_job, parse_job, is_ready, write_iteration
from bo_utils import setup_dirs
import time

INPUT_DIR = os.path.join(os.getcwd(), 'jobs')
OUTPUT_DIR = os.path.join(os.getcwd(), 'jobs')


def main(job_id, params):
    print('Job #%d' % job_id)
    print(params)
    job_dir = setup_dirs(job_id, INPUT_DIR)
    write_iteration(OUTPUT_DIR, job_id)
    create_job(job_id, params, job_dir)

    while not is_ready(job_id, OUTPUT_DIR):
        time.sleep(30)

    os.remove(os.path.join(OUTPUT_DIR, '{d}.done'.format(job_id)))
    result = parse_job(OUTPUT_DIR)
    time.sleep(5)
    print('Result = {:f}'.format(result))
    return {'result': result}


if __name__ == "__main__":
    print('testing')
    main(0, {"intermediate_dim": [8], "latent_dim": [2],
             "dec_h_activation": ["relu"],
             "dec_mean_activation": ["sigmoid"]})
