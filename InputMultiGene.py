import re
import sys

class InputMultiGene():
    def __init__(self):
        self.dna_dict = {}
        self.GeneName = ""
    
    def input_multi_gene(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            self.data = file.read().split()
            for i in range(0, len(self.data)):
                if re.match('^>Rosalind_', self.data[i]):
                    self.GeneName = re.sub('>', '', self.data[i])
                else:
                    if self.GeneName in self.dna_dict.keys() and re.match('^Rosalind_', self.GeneName):
                        self.dna_dict[self.GeneName] = self.dna_dict[self.GeneName] + self.data[i]
                    else:
                        self.dna_dict[self.GeneName] = self.data[i]
        

        return self.dna_dict

if __name__ == "__main__":
    multi_gene_dict = InputMultiGene().input_multi_gene(sys.argv[1])
    print(" --- ")
    for name, sequence in multi_gene_dict.items():
        print(name + ':' + sequence)