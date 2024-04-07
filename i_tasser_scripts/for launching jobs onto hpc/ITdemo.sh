#!/bin/bash

#PBS -P Project_Name_of_Job
#PBS -q short
#PBS -l select=1:ncpus=7:mpiprocs=7:mem=30GB
#PBS -j oe
#PBS -N Job_Name
source /app1/ebenv && module load jre/jdk-13 parallel

cd $PBS_O_WORKDIR


perl "/hpctmp/e0688551/I-tasser_install/I-TASSER5.2/I-TASSERmod/runI-TASSER.pl" -libdir "/hpctmp/e0688551/I-tasser-mtd-lib" -seqname "example" -datadir "/hpctmp/e0688551/I-tasser_install/72_outgroup/72_fasta_2" -runstyle "gnuparallel"