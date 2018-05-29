def main():
    a, b = map(int, input().split())

    print(calcurate(a, b))

def calcurate(x, y):
    sum = 0
    for i in range(x, y+1):
        if i % 2 != 0:
            sum += i
        else:
            pass
    
    return sum

if __name__ == "__main__":
    main()