#!/bin/bash

export EXP_NAME=$1
export DB_DIR="$(pwd)/$EXP_NAME/db"
mkdir $DB_DIR
echo $DB_DIR
mongod --fork --logpath $DB_DIR/mongodb.log --dbpath $DB_DIR
cd spearmint_py3
python main.py ../$EXP_NAME
