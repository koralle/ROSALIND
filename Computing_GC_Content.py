import re
import sys

class InputMultiGene():
    def __init__(self):
        self.dna_dict = {}
        self.GeneName = ""
    
    def inputGeneData(self, filename):
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

class Computing_GC_Content():
    
    def calcurate_GC(self, sequence):
        self.gc_dict = {'G':0, 'C':0}
        for symbol in sequence:
            if symbol == 'G':
                self.gc_dict['G'] += 1
            elif symbol == 'C':
                self.gc_dict['C'] += 1
        
        return (self.gc_dict['G'] + self.gc_dict['C']) / len(sequence)       

    

def main():
    dna_dict = InputMultiGene().inputGeneData(sys.argv[1])
    result_dict = {}
    max_name = ""
    max_gc = 0

    for name, sequence in dna_dict.items():
        result_dict[name] = Computing_GC_Content().calcurate_GC(sequence) * 100
        if max_gc <= result_dict[name]:
            max_name = name
            max_gc = result_dict[name]
    
    print(max_name)
    print(max_gc)
            

    

    
    




if __name__ == "__main__":
    main()