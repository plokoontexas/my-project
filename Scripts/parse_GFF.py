#!/usr/bin/env python3

import argparse
import gff_functions

def main():
    genome_sequence = gff_functions.read_fasta()
    print(genome_sequence)

    gff_functions.read_gff()
    gff_functions.write_output()
# Funtion to parse the command line arguments
def get_args():
    ###-------------- accept and parse command line arguments

    #create an argument parser object 

    parser = argparse.ArgumentParser(description="Get feature sequences from a gff file and corresponding genome file")
    # add a positional argument, in this case, the position of the Fibonacci sequece
    parser.add_argument("fasta", help="Name of genome file in FASTA format", type=str)
    parser.add_argument("gff3", help="Name of GFF3 file", type=str)


    args = parser.parse_args()
    return args

args = get_args()
# set the environment for this script
# is it main(), or is this a module being called by something else?
if __name__ == '__main__':
    main()