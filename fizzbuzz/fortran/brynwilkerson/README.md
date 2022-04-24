# Easy Instructions


Run `./run.sh N` from command line in `/fizzbuzz/brynwilkerson` with N being the max value of FizzBuzz.


# To Compile First

Follow these steps if the above doesn't work or if you want to edit the source code.

## To install GCC for Windows:
Follow these steps to install MinGW and add it to your PATH:
https://capsis.cirad.fr/capsis/documentation/mingw-installation

-When you get to the MinGW Installation Manager, 
the only package under Basic Set up that you need to 
select for Mark for Installation is mingw32-gcc-fortran

-Once you have completed the steps, you may need to restart your computer to
ensure that the PATH variables have been updated.

Run gfortran --version if you are unsure whether it is installed.

## Running the shell script:

Run the following commands in `/fizzbuzz/brynwilkerson`: 

```
gfortran -c fizz.f90

gfortran -c main.f90

gfortran -c tests.f90

gfortran -o fizzbuzz main.o fizz.o

gfortran -o tests tests.o fizz.o
```

Then running ```run.sh N``` should work.