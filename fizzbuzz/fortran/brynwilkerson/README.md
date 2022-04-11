# To install GCC for Windows:
Follow these steps to install MinGW and add it to your PATH:
https://capsis.cirad.fr/capsis/documentation/mingw-installation

-When you get to the MinGW Installation Manager, 
the only package under Basic Set up that you need to 
select for Mark for Installation is mingw32-gcc-fortran

-Once you have completed the steps, you may need to restart your computer to
ensure that the PATH variables have been updated.

Run gfortran --version if you are unsure whether it is installed.

# Running the shell script:
Run ./run.sh n in the command line, and replace n with the number you want to use.

# Error fixing:
If you get errors from ```./run.sh n``` then you may have to run commands manually first.

Run the following commands in /brynwilkerson: 

```
gfortran -c fizz.f90

gfortran -c main.f90

gfortran -c tests.f90

gfortran -o fizzbuzz main.o fizz.o

gfortran -o tests tests.o fizz.o
```

Then running ```run.sh n``` should work.