from __future__ import print_function
import os
import jinja2
from shutil import copy
import json

MAIN_SCRIPT = 'keras_test.py'


def create_paramjson(param, job_dir):
    p = {k: v[0] for k, v in param.items()}
    new_json = os.path.join(job_dir, 'params.json')
    with open(new_json, 'w') as fp:
        json.dump(p, fp)
    return


def create_odysseyjob(job_id, job_dir):
    template_file = 'templates/Job.sl'
    new_calc = os.path.join(job_dir, 'job.sl')
    calc_dict = {'n_cores': 1, 'n_nodes': 1, 'hour': 12}
    calc_dict['mem_cpu'] = 1000
    calc_dict['job_name'] = 'job_{:d}'.format(job_id)
    calc_dict['script_name'] = 'test.py'
    replace_textdict(template_file, new_calc, calc_dict)
    return


def create_job(job_id, param, job_dir):
    print('Creating job @ {}'.format(job_dir))
    create_odysseyjob(job_id, job_dir)
    # add any files you want to include on your job
    for i in [MAIN_SCRIPT]:
        copy('templates/{}'.format(i), job_dir)
    create_paramjson(param, job_dir)
    return


def is_ready(job_dir):
    # function is looking for this string
    # to indicate it has finished
    a_str = '**FINISHED**'
    job_file = os.path.join(job_dir, 'results.out')
    answer = False
    if os.path.exists(job_file):
        lines = open(job_file, 'r').read()
        answer = (lines.find(a_str) != -1)

    return answer


def parse_job(job_dir):
    # the parser is looking for this particular string
    # at the end of the file to parse out a result
    a_str = ' Final Result = '
    result_file = os.path.join(job_dir, 'results.out')

    for line in open(result_file, 'r').readlines():
        if a_str in line:
            result = float(line.replace(a_str, '').strip())

    return result

#======= Utility functions ========


def setup_dirs(job_id, adir):
    job_dir = os.path.join(adir, 'job_{:d}'.format(job_id))
    if not os.path.exists(job_dir):
        os.makedirs(job_dir)

    return job_dir


def write_iteration(adir, job_id):
    ite_file = os.path.join(adir, 'ite')
    with open(ite_file, 'w') as f:
        f.write(str(job_id))
    return


def read_iteration(adir):
    ite_file = os.path.join(adir, 'ite')
    if os.path.exists(ite_file):
        ite = int(open(ite_file).read().strip())
    else:
        ite = -1
    return ite


def replace_textdict(afile, bfile, adict):
    atxt = open(afile, 'r').read()
    btxt = jinja2.Environment().from_string(atxt).render(adict)
    open(bfile, 'w').write(btxt)
    return

if __name__ == "__main__":
    print('please import me')
