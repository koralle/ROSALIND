def main():
    string = input()
    dict = {"A":0, "C":0, "G":0, "T":0}

    for i in range(0, len(string)):
        dict[ string[i] ] += 1
    
    print("{} {} {} {}".format(dict["A"], dict["C"], dict["G"], dict["T"]))


if __name__ == "__main__":
    main()