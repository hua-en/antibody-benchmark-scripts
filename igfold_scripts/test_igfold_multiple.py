from igfold import IgFoldRunner
from igfold.refine.pyrosetta_ref import init_pyrosetta
from igfold.utils.visualize import *

init_pyrosetta()

sequence1 = {
    "H": "MRCVGVGNRDFVEGVSGGAWVDLVLEHGGCVTTMAQGKPTLDFELTKTTAKEVALLRTYCIEASISNITTATRCPTQGEPYLKEEQDQQYICRRDVVDRGWGNGCGLFGKGGVVTCAKFSCSGKITGNLVQIENLEYTVVVTVHNGDTHAVGNDTSNHGVTAMITPRSPSVEVKLPDYGELTLDCEPRSGIDFNEMILMKMKKKTWLVHKQWFLDLPLPWTAGADTSEVHWNYKERMVTFKVPHAKRQDVTVLGSQEGAMHSALAGATEVDSGDGNHMFAGHLKCKVRMEKLRIKGMSYTMCSGKFSIDKEMAETQHGTTVVKVKYEGAGAPCKVPIEIRDVNKEKVVGRIISSTPLAENTNSVTNIELEPPFGDSYIVIGVGNSALTLHWFRKG",
    # "L": "YVLGQSSSMSVAPGQTAKISCWGYYMGTKPVNWYQLKPGRAPSLIISYDDERASGTPARFSGSHSGSTATLTISNVVPADEADYFCQVWDSKYEEIYFGGGTALTVLGQPKAAPSVTLFPPSSEELQANKATLVCLISDFYPGAVTVAWKADSSPVKAGVETTTPSKQSNNKYAASSYLSLTPEQWKSHRSYSCQVTHEGSTVEKTVAP"
}

sequence2 = {
    "H": "MAEVQLVESGAEVKKPGASVKVSCKASGYTFTSYAMHWVRQAPGQRLEWMGWINAGNGNTKYSQKFQDRVTITRDTSASTAYMELSSLRSEDTAIYYCARDKVDDYGDYWFPTLWYFDYWGQGTLVTVSSGTGGSGGGGSGGGG"
}

sequence3 = {
    "H":"EVQLVESGAEVKKPGASVKVSCKASGYTFTSYAMHWVRQAPGQRLEWMGWINAGNGNTKYSQKFQDRVTITRDTSASTAYMELSSLRSEDTAIYYCARDKVDDYGDYWFPTLWYFDYWGQGTLVTVSS"
}

pred_pdb = "7A3Q_1_predicted.pdb"

igfold = IgFoldRunner()
igfold.fold(
    "7A3Q_1-predicted.pdb", # Output PDB file
    sequences=sequence1, # Antibody sequences
    do_refine=True, # Refine the antibody structure with PyRosetta
    do_renum=False, # Renumber predicted antibody structure (Chothia)
)
igfold.fold(
    "7A3Q_2-predicted.pdb", # Output PDB file
    sequences=sequence2, # Antibody sequences
    do_refine=True, # Refine the antibody structure with PyRosetta
    do_renum=False, # Renumber predicted antibody structure (Chothia)
)
igfold.fold(
    "7A3Q_2-short-predicted.pdb", # Output PDB file
    sequences=sequence3, # Antibody sequences
    do_refine=True, # Refine the antibody structure with PyRosetta
    do_renum=False, # Renumber predicted antibody structure (Chothia)
)

