import subprocess

def compare_proteins(original: str, predicted: str) -> tuple[float, float]:
    result = subprocess.run(['TMalign', original, predicted, '-outfmt', '2'], stdout=subprocess.PIPE)
    result_str = result.stdout.decode('utf-8')
    result_val = result_str.split('\n')[1].split('\t')
    TMscore = float(result_val[2])
    RMSD = float(result_val[4])
    return (TMscore, RMSD)