import sys
import re

class InputSingleGene():
    def __init__(self):
        self.gene_dict = {}

    def input_single_gene(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            data = file.read().split()
            data[0] = re.sub('>', '', data[0])
            self.gene_dict[data[0]] = data[1]

        return self.gene_dict

def main():
    gene_dict = InputSingleGene().input_single_gene(sys.argv[1])
    print(gene_dict)

if __name__ == "__main__":
    main()

        