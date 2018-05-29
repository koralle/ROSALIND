class Codon():
    def __init__(self):
        self.bases = "UCAG"
        self.codons = [base1+base2+base3 for base1 in self.bases for base2 in self.bases for base3 in self.bases]
        self.aminoacids = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
        self.codon_table = dict(zip(self.codons, self.aminoacids))

    def base_to_protein(self, codon):
        return self.codon_table[codon]

class Translate():
    def __init__(self):
        self.protein_string = ""
        self.translate_flag = 0
        self.start = 0
        

    def find_methionine(self, rna):
        codon = Codon()
        for i in range(2, len(rna)):
            if codon.codon_table[rna[i-2:i+1]] == "M":
                return i-2

    def Translate_RNAstring(self, rna):
        codon = Codon()
        self.start = self.find_methionine(rna)
        for i in range(self.start, len(rna),3):
            if codon.base_to_protein(rna[i:i+3]) == '*':
                break
            else:
                self.protein_string += codon.base_to_protein(rna[i:i+3])
        return self.protein_string
        
def main():
    with open("rosalind_prot.txt", "r", encoding="utf-8") as file:
        rna_string = file.read()
    translate = Translate()
    print( translate.Translate_RNAstring(rna_string) )

if __name__ == "__main__":
    main()