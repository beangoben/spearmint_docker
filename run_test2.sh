#!/bin/bash

source activate python2
export EXP_NAME=test
export DB_DIR="$(pwd)/$EXP_NAME/db"
mkdir -p $DB_DIR
echo $DB_DIR
mongod --fork --logpath $DB_DIR/mongodb.log --dbpath $DB_DIR
cd py2
python main.py ../$EXP_NAME
