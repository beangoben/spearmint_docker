from __future__ import print_function
import os
from bo_utils import create_job, parse_job, not_ready
import time

INPUT_DIR = os.path.join(os.getcwd(), 'Jobs', 'inbox')
OUTPUT_DIR = os.path.join(os.getcwd(), 'Jobs', 'completed')


def main(job_id, params):
    print('Job #%d' % job_id)
    print(params)
    create_job(job_id, params, INPUT_DIR)
    run_dir = os.path.join(OUTPUT_DIR, 'job_{:d}'.format(job_id))

    while not_ready(job_id, run_dir):
        time.sleep(30)

    result = parse_job(job_id, run_dir)
    print('Result = {:f}'.format(result))
    return {'result': result}

if __name__ == "__main__":
    print('testing')
    main(0, {"intermediate_dim": [8], "latent_dim": [2],
             "dec_h_activation": ["relu"],
             "dec_mean_activation": ["sigmoid"]})
