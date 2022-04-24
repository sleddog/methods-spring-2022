#!/bin/bash
cobc -free -x -o FizzBuzz-exe FizzBuzz
echo "Begin shell script execution."
echo $1 | ./FizzBuzz-exe
rm FizzBuzz-exe

