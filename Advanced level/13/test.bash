#! /bin/bash

if [ $# -eq 2 ]
then
    echo "Hello, $1 $2! Nice to see you here!"
else
    echo "Missing arguments or to many arguments, check input parameters!"
fi
