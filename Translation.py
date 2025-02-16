from Bio.Seq import Seq

def translate_dna(dna_sequence: str) -> str:
    """
    Translates a DNA sequence into a protein sequence using the standard genetic code.
    
    Args:
        dna_sequence (str): Input DNA sequence (A, T, C, G).
        
    Returns:
        str: Translated protein sequence.
    """
    dna_seq = Seq(dna_sequence)
    protein_seq = dna_seq.translate(to_stop=True)  # Stops at stop codon
    return str(protein_seq)

# Example usage:
dna_sample = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
print(translate_dna(dna_sample))  # Output: MAMIVMGR*
