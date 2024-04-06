from igfold import IgFoldRunner
from igfold.refine.pyrosetta_ref import init_pyrosetta
from igfold.utils.visualize import *

init_pyrosetta()

sequences = {
    "H": "EVQLVQSGPEVKKPGTSVKVSCKASGFTFMSSAVQWVRQARGQRLEWIGWIVIGSGNTNYAQKFQERVTITRDMSTSTAYMELSSLRSEDTAVYYCAAPYCSSISCNDGFDIWGQGTMVTVS",
    "L": "DVVMTQTPFSLPVSLGDQASISCRSSQSLVHSNGNTYLHWYLQKPGQSPKLLIYKVSNRFSGVPDRFSGSGSGTDFTLKISRVEAEDLGVYFCSQSTHVPYTFGGGTKLEIK"
}
pred_pdb = "my_antibody.pdb"

igfold = IgFoldRunner()
igfold.fold(
    pred_pdb, # Output PDB file
    sequences=sequences, # Antibody sequences
    do_refine=True, # Refine the antibody structure with PyRosetta
    do_renum=True, # Renumber predicted antibody structure (Chothia)
)
show_pdb(pred_pdb, len(sequences), bb_sticks=False, sc_sticks=True, color="rainbow")
