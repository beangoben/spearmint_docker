# Supercomputer BO optimizer
These scripts are made to run spearmint as a bayesian optimizer on a local machine as a docker image.
Job files are created and monitored and then results parsed out to create new jobs.
To use it, you will want to modify **ody_utils.py**. Following are the steps to run it.

## Edit ody_utils and templates

* **ody_bo.py** is the bo file that imports **ody_utils.py** to do the whole bo loop. Not much editing is needed here.
* **ody_utils.py** is a python module used in ody_bo.py, it has functions for 1) creating all the job files (`create_job(job_id, param, job_dir)`), 2) parsing calculations for results (`parse_job(job_id, job_dir)`)  and 3) determine when a calculation is ready to be parsed (`not_ready(job_id, job_dir)`). Also contains other utility functions.
* **templates** if a folder with template files for a normal job. **ody_utils.py** uses jinja2 to do text replacement on several files.
* **config.json** hyperparameter space to explore.


## Run your job_manager
Assuming you are in a directory inside of your favorite supercomputer (maybe odyssey)
you run a command to start your automated job submitter, for example:
```
python job_manager.py --root=path_to_jobs/jobs
```
## Mount virtual drive locally

Using sshfs:

```
sshfs user@domain:path_to_jobs/jobs "$(pwd)"/jobs
```

## Run docker image on this folder

```
./run_spearmint.sh ody_bo 8890
```
