import Transcription, Codon, Translate
import InputSingleGene
import sys

class DNAtoProtein():
    def __init__(self):
        self.dna_string = ""
        self.rna_string = ""
        self.protein_string = ""
        
    def dna_to_protein(self, dna_string):
        self.dna_string = dna_string
        self.rna_string = Transcription.Transcription().transctiprion(self.dna_string)
        self.protein_string = Translate.Translate().translate(self.rna_string)

        return self.protein_string

if __name__ == "__main__":
    gene_dict = InputSingleGene.InputSingleGene().input_single_gene(sys.argv[1])
    for sequence in gene_dict.values():
        print (DNAtoProtein().dna_to_protein(sequence) )
