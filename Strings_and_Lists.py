def main():
    query = input()
    a, b, c, d = map(int, input().split())

    print(slice(query, a, b, c, d))

def slice(str, x, y, z, w):
    output1 = str[x:y+1]
    output2 = str[z:w+1]

    return output1 + " " + output2

if __name__ == "__main__":
    main()