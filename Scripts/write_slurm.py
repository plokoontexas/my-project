#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description="This script adds the intial Slurm info")

parser.add_argument("job_name", help="Name of the Job")

parser.add_argument("hours", help="Number of Hours", type=int)

parser.add_argument("que", help="Which que do you want to use")

email = "jp297@uark.edu"

args = parser.parse_args()

print("#!/bin/bash")
print(f"#SBATCH --job-name={args.job_name}")
print(f"#SBATCH --time={args.hours}:00:00")
print(f"#SBATCH --partition {args.que}")
print("#SBATCH -q cloud")
print("#SBATCH -N 1")
print("#SBATCH -n 1")
print("#SBATCH -c 1")
print(f"#SBATCH --mail-user={email}")
print("")
print("module load blast")
print("")
print("blastn -query watermelon.fsa -subject watermelon.fsa > wat.vs.wat.blastn")



