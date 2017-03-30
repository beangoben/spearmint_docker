#!/bin/bash

DOCKER_IMG='beangoben/spearmint_docker'
EXP_NAME=$1
# port for jupyter
if [ -z "$2" ] 
then PORT=8888
else PORT=$2
fi
SCRIPT="./run_experiment.sh"

#echo $EXP_NAME 
#echo $PY
#echo $PORT 
#echo $SCRIPT
docker run -p $PORT:8888 -v "$(pwd)":/home/jovyan/work -it $DOCKER_IMG start.sh $SCRIPT $EXP_NAME

