import re

class CountingPointMutations(object):
    def __init__(self):
        self.__mismatch = 0
    
    def counting_point_mutations(self, string1, string2):
        for i in range(0, len(string1)):
            if string1 == string2[i]:
                pass
            else:
                self.__mismatch += 1

        return self.__mismatch

def main():
    with open("rosalind_hamm.txt", "r", encoding="utf-8") as file:
        string1 = file.readline()
        string2 = file.readline()

    print(check(string1, string2))

def check(str1, str2):
    mismatch = 0

    for i in range(0, len(str1)):
        if str1[i] == str2[i]:
            pass
        else:
            mismatch += 1

    return mismatch

if __name__ == "__main__":
    main()