#!/bin/bash

# variables for the job
JOB_NAME={{job_name}}
SCRIPT={{script_name}}

# run python script
echo "running python"
python ${SCRIPT} > results.out