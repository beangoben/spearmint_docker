from __future__ import print_function
import os
import jinja2
from ody_utils import create_job, parse_job


def replace_textdict(afile, bfile, adict):
    atxt = open(afile, 'r').read()
    btxt = jinja2.Environment().from_string(atxt).render(adict)
    open(bfile, 'w').write(btxt)
    return


def create_odysseyjob(job_id, job_dir):
    template_file = 'Job_template.sl'
    new_calc = os.path.join(job_dir, 'job.sh')
    calc_dict = {'n_cores': 1, 'n_nodes': 1, 'hour': 12}
    calc_dict['mem_cpu'] = 1000
    calc_dict['job_name'] = 'job_{:d}'.format(job_id)
    calc_dict['script_name'] = 'test.py'
    replace_textdict(template_file, new_calc, calc_dict)
    return


def create_job(job_id, param, job_dir):
    new_dir = os.path.join(job_dir, 'job_{:d}'.format(job_id))
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    create_odysseyjob(job_id, job_dir)
    # create files

    return


def not_ready(job_id, job_dir):
    a_str = '**FINISHED**'
    job_file = os.path.join(job_dir, 'results.out')
    lines = open(job_file, 'r').read()
    answer = lines.find(a_str)
    return answer


def parse_job(job_id, job_dir):
    a_str = ' Final Result = '
    result_file = os.path.join(
        job_dir, 'job_{:d}'.format(job_id), 'results.out')
    for line in open(result_file, 'r').readlines():
        if a_str in line:
            result = float(line.replace(a_str, '').strip())

    return result

if __name__ == "__main__":
    print('please import me')
