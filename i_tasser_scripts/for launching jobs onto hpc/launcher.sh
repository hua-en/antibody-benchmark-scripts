#!/bin/bash

for i in {1..77}
do
    qsub -v dir="/hpctmp/e0688551/I-tasser_install/72_n_out/72_fasta_$i" /hpctmp/pbs_dm_stage/access_temp_stage/e0688551/ITasser-pdcode/ITdemo2.sh
done