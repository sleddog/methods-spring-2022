#!/bin/bash
cobc -free -x -o FizzBuzzMod-exe FizzBuzzMod
echo "Begin shell script execution."
echo $1 | ./FizzBuzzMod-exe
rm FizzBuzzMod-exe
