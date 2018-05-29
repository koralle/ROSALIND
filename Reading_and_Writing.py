def main():
    with open("rosalind_ini5.txt", "r", encoding="utf-8") as file:
        num_line = 1
        for line in file:
                if num_line % 2 == 0:
                    print(line, end='')
                else:
                    pass
                num_line += 1

if __name__ == "__main__":
    main()