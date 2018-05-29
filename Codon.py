class Codon():
    def __init__(self):
        self.bases = "UCAG"
        self.codons = [base1+base2+base3 for base1 in self.bases for base2 in self.bases for base3 in self.bases]
        self.aminoacids = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
        self.codon_table = dict(zip(self.codons, self.aminoacids))

    def base_to_protein(self, codon):
        return self.codon_table[codon]

        
if __name__ == "__main__":
    codon = Codon()
    print (codon.codon_table)
        