import string

def main():
    
    with open("rosalind_revc.txt", "r", encoding="utf-8") as file:
        template_string = file.read()

    complement_string = template_string.translate(str.maketrans('ATGC', 'TACG'))[::-1]
    
    print(complement_string)


if __name__ == "__main__":
    main()