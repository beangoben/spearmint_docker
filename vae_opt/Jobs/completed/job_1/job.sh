#!/bin/bash

# variables for the job
JOB_NAME=job_1
SCRIPT=keras_test.py

# run python script
echo "running python"
python ${SCRIPT} > results.out

# LINES BELOW ARE ADDED AUTOMATICALLY BY JOB MANAGER #
touch job_manager-complete

