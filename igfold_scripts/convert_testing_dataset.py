from abnumber import Chain
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import pandas as pd
import os
import shutil

os.chdir("testing_fasta_dataset")
all_fasta_files = []

# Create shortened fasta files for each fasta file
for fasta_file in os.listdir("."):
    for record in SeqIO.parse(fasta_file, "fasta"):
        cur_record = [record.id, "?", "?"]
        cur_record.append(str(record.seq))
        try:
            cur_chain = Chain(str(record.seq), "chothia")
            cur_record.append(cur_chain.seq)
            new_fasta_file_record = SeqRecord(Seq(cur_chain.seq), id=record.id, name=record.name, description=record.description)
            new_fasta_file_path = os.path.join("..", "testing_fasta_dataset_shortened", record.id + "-short.fasta")
            SeqIO.write(new_fasta_file_record, new_fasta_file_path, "fasta")
        except Exception as e:
            cur_record.append(None)
        
        all_fasta_files.append(cur_record)
        
# Shorten created fasta files to 2 lines
os.chdir("..")
os.chdir("testing_fasta_dataset_shortened")
for short_fasta_file in os.listdir("."):
    with open(short_fasta_file, "r") as f:
        txt = f.read().split("\n")
        full_seq = ""
        for line in txt[1:]:
            full_seq += line
        title = txt[0]
        
    with open(short_fasta_file, "w") as f:
        f.write(title + "\n")
        f.write(full_seq)

os.chdir("..")

fasta_df = pd.DataFrame(all_fasta_files, columns=["name", "type", "heavy_or_light", "old_seq", "new_seq"])
fasta_df.to_csv("all_fasta.csv")