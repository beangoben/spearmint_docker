# VAE BO optimizer
These scripts are made to run spearmint as a bayesian optimizer on a local machine as a docker image, while optimizing the hyperparameters
for a variational autoencoder on MNIST data, also on your local machine

To use it, you will want to modify **bo_utils.py**. Following are the steps to run it.

## Edit bo_utils and templates

* **bo_loop.py** is the bo file that imports **bo_utils.py** to do the whole bo loop. Not much editing is needed here.
* **bo_utils.py** is a python module used in bo_loop.py, it has functions for 1) creating all the job files (`create_job(job_id, param, job_dir)`), 2) parsing calculations for results (`parse_job(job_id, job_dir)`)  and 3) determine when a calculation is ready to be parsed (`not_ready(job_id, job_dir)`). Also contains other utility functions.
* **templates** if a folder with template files for a normal job. **bo_utils.py** uses jinja2 to do text replacement on several files.
* **config.json** hyperparameter space to explore.

## Run a local job manager

```
python job_manager.py -r "$(pwd)"/vae_opt/Jobs -s
python job_manager.py -r "$(pwd)"/vae_opt/Jobs -e engines.LocalEngine -p2
```

## Run docker image on this folder

```
./run_spearmint.sh vae_opt 8890
```
