#!/bin/bash
pwd
mvn test
nosetests
pwd
python ./scripts/test.py


