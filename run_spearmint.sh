#!/bin/bash

DOCKER_IMG='beangoben/spearmint_docker'
EXP_NAME=$1
# python version
if [ -z "$2" ]
then PY='py2'
else PY=$2
fi
# port for jupyter
if [ -z "$3" ] 
then PORT=8888
else PORT=$3
fi
SCRIPT="./run_experiment_$PY.sh"

#echo $EXP_NAME 
#echo $PY
#echo $PORT 
#echo $SCRIPT
docker run -p $PORT:8888 -v "$(pwd)":/home/jovyan/work -it $DOCKER_IMG start.sh $SCRIPT $EXP_NAME

