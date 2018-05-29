def main():
    """dna_string = input()
    dna_motif  = input()"""

    with open("rosalind_subs.txt", "r", encoding="utf-8") as file:
        data = file.read()
        dna_string = data.split()[0]
        dna_motif  = data.split()[1]
    
    list = map(str, find_motif(dna_string, dna_motif))
    output = ' '.join(list)

    print(output)


def find_motif(dna, motif):
    list_position = []
    for i in range(0, len(dna)):
        if dna[i:i+len(motif)] == motif:
            list_position.append(i+1)            
        else:
            pass

    return list_position


if __name__ == "__main__":
    main()