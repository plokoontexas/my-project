#!/bin/bash
#SBATCH --job-name=blast_job
#SBATCH --time=02:00:00:00:00
#SBATCH --partition cloud72
#SBATCH -q cloud
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -c 1
#SBATCH --mail-user=jp297@uark.edu

module load blast

blastn -query watermelon.fsa -subject watermelon.fsa > wat.vs.wat.blastn
