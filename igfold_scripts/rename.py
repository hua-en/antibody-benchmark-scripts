import os
import shutil

src_dir = "pure_fasta_results"
dst_dir = src_dir + "_renamed"

fd = os.listdir(src_dir)
print(fd)

if not os.path.exists(dst_dir):
    os.mkdir(dst_dir)

for f in fd:
    x = f.split(".")
    new_name = x[0] + "_igfold" + ".pdb"
    shutil.copyfile(os.path.join(src_dir, f), os.path.join(dst_dir, new_name))