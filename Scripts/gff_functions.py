#gff functions

import csv

def read_fasta(fasta_file):
    #make a varialble for the genome sequence
    seq = ''
    with open(fasta_file, "r") as f:
        for line in f: 
            if line.startswith(">"):
                continue
            else: 
                seq += line.strip()
    return seq

    

def read_gff(gff3_file):
    with open(gff3_file, "r") as g:
        reader = csv.reader(gff3_file, delimiter='\t')
        for line in reader:
            start = line[3]
            end = line[4]
            atts = line[8]
            print(start,end,atts)



def write_output():
    print("inside write_output")


