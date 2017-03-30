from __future__ import print_function
import numpy as np


def branin(x, y):
    result = np.square(y - (5.1 / (4 * np.square(np.pi))) * np.square(x) +
                       (5 / np.pi) * x - 6) + 10 * (1 - (1. / (8 * np.pi))) * np.cos(x) + 10
    return float(result)


def main(job_id, params):
    print('Job #%d' % job_id)
    print(params)
    result = branin(params['x'], params['y'])
    print('Result = %f' % result)
    return result
