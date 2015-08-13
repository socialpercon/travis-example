#!/bin/bash
pwd
ps -ef | grep mysql
mvn test
nosetests
pwd
python ./scripts/test.py


