# igfold_scripts

Scripts used for the running of IgFold and the processing of data with TMAlign.

- tmalign_python: A quick python function to call the TMalign program on two pdb files.
- test_igfold and test_igfold_multiple: Test scripts to run igfold on single and multiple sequences.
- convert_training_dataset: A script to shorten a set of fasta files with AbNumber as well as compile all sequences into a CSV file.
- auto_igfold: A script that takes the CSV file from convert_training_dataset, runs IGFold on all sequences, compares predicted sequences with TMalign and compiles all results into a CSV file.
- rename: Renames all pdb files in a folder.