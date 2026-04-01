#!/usr/bin/env python3

import argparse

# Funtion to parse the command line arguments
def get_args():
    ###-------------- accept and parse command line arguments

    #create an argument parser object 

    parser = argparse.ArgumentParser(description="This script calculates the number at a given positon \
                                    in the Fibonacci sequence")
    # add a positional argument, in this case, the position of the Fibonacci sequece
    parser.add_argument("position", help="Position in the Fibonacci sequence", type=int)

    #add optional argument for verbose output or not 
    #if store true this meands assign true if the optional argument is specified on the commandline, so the default for 'store_true' is actually false
    parser.add_argument("-v", "--verbose", help="Print verbose output", action='store_true')

    #parse the arguments

    args = parser.parse_args()
    return args

###------ Functuion to calculate the fibonacci 
def fib():

    a, b = 0, 1

    for i in range(int(pheobe.position)):
        a, b = b, a + b

    fibonacci_number = a
    return fibonacci_number

#Function to print output
def print_output(output):
    if pheobe.verbose:
        print(f"The Fibonacci number for {pheobe.position} is {output}")
    else: 
        print(output)


###--- define the main function
def main():
    fib_num = fib()
    print_output(fib_num)

###--- calling get_args() happens out here on its own 
pheobe = get_args()

# set the environment for this script 
# is this main or 
# is this a python module being called by another script
if __name__ == '__main__':
    main()