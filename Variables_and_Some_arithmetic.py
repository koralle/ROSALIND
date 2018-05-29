def main():
    num1, num2 = map(int, input().split())
    print( calcurate(num1, num2) )

def calcurate(x, y):
    return x ** 2 + y ** 2

if __name__ == "__main__":
    main()