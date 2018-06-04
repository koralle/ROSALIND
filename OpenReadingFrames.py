import InputSingleGene
import sys
import Translate, Codon, Transcription

class OpenReadingFrames(Translate.Translate):
    def __init__(self, dna_string):
        super(OpenReadingFrames, self).__init__(dna_string)
        
    def OpenReadingFrames(self):
        self.rna_string = Transcription.Transcription().transctiprion(self.dna_string)
        for i in range(0, len(self.rna_string)):
            



def main():
    gene_dict = InputSingleGene.InputSingleGene().input_single_gene(sys.argv[1])
    for name, sequence in gene_dict.items():
        OpenReadingFrames(sequence).OpenReadingFrames()

if __name__ == "__main__":
    main()