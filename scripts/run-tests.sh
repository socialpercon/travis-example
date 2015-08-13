#!/bin/bash
pwd
echo $FOO $BAR
ps -ef | grep mysql
mvn test
nosetests
pwd
python ./scripts/test.py


