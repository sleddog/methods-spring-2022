#!/bin/sh

echo "Running FizzBuzz"
gfortran -o fizzbuzz.exe fizzbuzz.f90
./fizzbuzz.exe $1
