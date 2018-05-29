import re
import TheGeneticCode

class Splicing():
    def splicing_rna(self, dna_seq, IntronList):
        self.premRNA = re.sub("T", "U", dna_seq)
        for i in range(0, len(IntronList)):
            IntronList[i] = re.sub("T", "U", IntronList[i])
            self.premRNA = re.sub(IntronList[i], "", self.premRNA)
        
        self.spliced_rna = self.premRNA
        return self.spliced_rna


def main():
    intron_list = []
    with open("rosalind_splc.txt", "r", encoding="utf-8") as file:
        data = file.read().split()
        templateDNA_seq = data[1]
        # Intron Data -------
        i = 3
        while i <= len(data)-1:
            intron_list.append(data[i])
            i += 2

    spliced_rna = Splicing().splicing_rna(templateDNA_seq, intron_list)
    print(TheGeneticCode.Translate().Translate_RNAstring(spliced_rna))

if __name__ == "__main__":
    main()