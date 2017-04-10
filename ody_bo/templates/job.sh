#!/bin/bash

#SBATCH -n {{n_cores}}                # Number of cores
#SBATCH -N {{n_nodes}}                # Ensure that all cores are on one machine
#SBATCH -t 0-{{hours}}:00         # Runtime in D-HH:MM
#SBATCH -p aspuru-guzik       # Partition to submit to
#SBATCH --mem-per-cpu={{mem_cpu}}           # Memory pool for all cores (see also --mem-per-cpu)
#SBATCH -J {{job_name}}

# define variables
module load gcc/4.9.3-fasrc01 tensorflow/1.0.0-fasrc03
# custom anaconda env
source activate keras_cpu
# variables for the job
JOB_NAME={{job_name}}
SCRIPT={{script_name}}
CUR_DIR=$(pwd)
SCRATCH=/scratch
RESULTS=$(pwd)

#Create start dummy file
touch $CUR_DIR/$JOB_NAME.start

echo "setuping up directories"
echo "  at ${JOB_NAME}/${SLURM_JOB_ID}"
#setup scratch dirs
cd $SCRATCH
mkdir -p bo_${JOB_NAME}/${SLURM_JOB_ID}
cd ${JOB_NAME}/${SLURM_JOB_ID}
cp -v ${CUR_DIR}/${SCRIPT} .
cp -v ${CUR_DIR}/params.json .

# run python script
echo "running python"
python ${SCRIPT} > results.out 2>&1
# move results of calc
echo "copy results"
mv results.out $RESULTS

#Create finished dummy file:
touch $CUR_DIR/$JOB_NAME.done
