import subprocess
import os, shutil
import pandas as pd

def compare_proteins(original: str, predicted: str) -> tuple[float, float]:
    result = subprocess.run(['TMalign', original, predicted, '-outfmt', '2'], stdout=subprocess.PIPE)
    result_str = result.stdout.decode('utf-8')
    print(result_str)
    result_val = result_str.split('\n')[1].split('\t')
    TMscore = max(float(result_val[2]),float(result_val[3]))
    RMSD = float(result_val[4])
    return [TMscore,RMSD]

#it_modeldir = "/mnt/c/Users/Lenovo/Downloads/7AMP_1.pdb"
#actualmodeldir = "/mnt/c/Users/Lenovo/Downloads/TMalign_72/actual_pdb_structures/7AMP.pdb"

currentdir = "/mnt/c/Users/Lenovo/Downloads/TMalign_72"
predicteddir = "/mnt/c/Users/Lenovo/Downloads/TMalign_72/short_notintrain_IT"
actualdir = "/mnt/c/Users/Lenovo/Downloads/TMalign_72/actual_pdb_structures"
predictedlst = os.listdir(predicteddir)
print(predictedlst)
df_0 = []
name = []


for p_pdb in predictedlst:
    p_pdb_dir = predicteddir + "/" + p_pdb
    actual_name = p_pdb.split("_")[0] + ".pdb"
    actual_dir = actualdir + "/" + actual_name
    #print(p_pdb_dir, actual_dir)
    df_row = compare_proteins(actual_dir, p_pdb_dir)
    df_0.append(df_row)
    name.append(p_pdb[:-4])
    print(predictedlst.index(p_pdb))

'''
antibody_list = os.listdir("/mnt/c/Users/Lenovo/Downloads/TMalign_72/pure_antibody_TEST/Pure Test")
for p_pdb in antibody_list:
    p_pdb_dir = predicteddir + "/" + p_pdb[:-6] + ".pdb"
    actual_name = p_pdb.split("_")[0] + ".pdb"
    actual_dir = actualdir + "/" + actual_name
    #print(p_pdb_dir, actual_dir)
    df_row = compare_proteins(actual_dir, p_pdb_dir)
    df_0.append(df_row)
    name.append(p_pdb[:-4])
'''

df = pd.DataFrame(df_0, index=name, columns=["TMscore","RMSD"])
df.to_excel("/mnt/c/Users/Lenovo/Downloads/TMalign_72/corrected.xlsx")



