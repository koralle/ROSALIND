def main():
    CountDict = {}
    with open("rosalind_ini6.txt", "r", encoding="utf-8") as file:
        data = file.read()
        word_list = data.split()
    # ------
        key_count(CountDict, word_list)
        result(CountDict)

def key_count(dict, list):
    for word in list:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    
def result(dict):
    for word, count in dict.items():
        print('{} {}'.format(word, count))
    
if __name__ == "__main__":
    main()