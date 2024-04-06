# %%
import subprocess
from igfold import IgFoldRunner
from igfold.refine.pyrosetta_ref import init_pyrosetta
from igfold.utils.visualize import *
import pandas as pd
import os

init_pyrosetta()

def compare_proteins(predicted: str, original: str) -> tuple[float, float]:
    result = subprocess.run(['TMalign', predicted, original, '-outfmt', '2'], stdout=subprocess.PIPE)
    result_str = result.stdout.decode('utf-8')
    result_val = result_str.split('\n')[1].split('\t')
    TMscore = float(result_val[2])
    RMSD = float(result_val[4])
    return (TMscore, RMSD)

testing_dataset_df = pd.read_csv("all_fasta_edited.csv")

# %%
igfold = IgFoldRunner()
results_list = []

for index, row in testing_dataset_df.iterrows():
    print(f"Running IgFold for {row["name"]}...")
    new_seq_len = None if pd.isnull(row["new_seq"]) else len(row["new_seq"])
    cur_entry = [row["name"], row["type"], len(row["old_seq"]), new_seq_len]
    pure_name = row["name"].split("_")[0]
    
    # First igfold run
    output_file_name = row["name"] + "-predicted.pdb"
    igfold.fold(
        os.path.join(".", "testing_fasta_results", output_file_name), # Output PDB file
        sequences={row["heavy_or_light"]: row["old_seq"]}, # Antibody sequences
        do_refine=True, # Refine the antibody structure with PyRosetta
        do_renum=False, # Renumber predicted antibody structure (Chothia)
    )
    # First tmalign comparison
    cur_tmscore, cur_rmsd = compare_proteins(os.path.join(".", "testing_fasta_results", output_file_name),
                                             os.path.join(".", "actual_pdb_structures", pure_name + ".pdb"))
    cur_entry.append(cur_tmscore)
    cur_entry.append(cur_rmsd)
    
    # If there is no shortened sequence, continue
    if pd.isnull(row["new_seq"]):
        cur_entry.append(None)
        cur_entry.append(None)
        results_list.append(cur_entry)
        continue

    # Second igfold run
    output_file_name_light = row["name"] + "-short-predicted.pdb"
    igfold.fold(
        os.path.join(".", "testing_fasta_results", output_file_name_light), # Output PDB file
        sequences={row["heavy_or_light"]: row["new_seq"]}, # Antibody sequences
        do_refine=True, # Refine the antibody structure with PyRosetta
        do_renum=False, # Renumber predicted antibody structure (Chothia)
    )    
    
    # Second tmalign comparison
    cur_tmscore_short, cur_rmsd_short = compare_proteins(os.path.join(".", "testing_fasta_results", output_file_name_light),
                                                         os.path.join(".", "actual_pdb_structures", pure_name + ".pdb"))
    
    cur_entry.append(cur_tmscore_short)
    cur_entry.append(cur_rmsd_short)
    results_list.append(cur_entry)

results_df = pd.DataFrame(results_list, columns=["name", "type", "old_seq_len", "new_seq_len", "regular_tmscore", "regular_rmsd", "shorter_tmscore", "shorter_rmsd"])
results_df.to_csv("testing_results.csv")