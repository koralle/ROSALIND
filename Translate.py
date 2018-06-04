import Codon
import sys 
import InputSingleGene, Transcription
class Translate():

    def __init__(self, dna_string):
        self.dna_string = dna_string
        self.codon = Codon.Codon()

    def find_methionine(self, rna_string):
        for i in range(2, len(rna_string)):
            if Codon.Codon().codon_table[rna_string[i-2:i+1]] == "M":
                return i-2
                
    def translate(self, rna_string, start):
        self.protein_string = ""
        for i in range(start, len(rna_string),3):
            if self.codon.base_to_protein(rna_string[i:i+3]) == '*':
                break
            else:
                self.protein_string += self.codon.base_to_protein(rna_string[i:i+3])
        
        return self.protein_string

if __name__ == "__main__":
    gene_dict = InputSingleGene.InputSingleGene().input_single_gene(sys.argv[1])

    for name, sequence in gene_dict.items():
        translate = Translate(sequence)
        rna_seq = Transcription.Transcription().transctiprion(sequence)
        start = translate.find_methionine(rna_seq)
        protein_seq = translate.translate(rna_seq, start)

        print(protein_seq)