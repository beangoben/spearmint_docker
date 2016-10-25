#!/bin/bash

export EXP_NAME=objective
export DB_DIR="$(pwd)/$EXP_NAME/db"
echo $DB_DIR
mongod --fork --logpath $DB_DIR/mongodb.log --dbpath $DB_DIR
cd spearmint
python main.py ../$EXP_NAME
