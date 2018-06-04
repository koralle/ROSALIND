import InputSingleGene
import sys

def main():
    dna_dict = InputSingleGene.InputSingleGene().input_single_gene(sys.argv[1])


    for name in dna_dict.keys():
        template_string = dna_dict[name]
        complement_string = template_string.translate(str.maketrans('ATGC', 'TACG'))[::-1]

    print(template_string)
    print(complement_string)

if __name__ == "__main__":
    main()