dict = {}
def main():
    n, k = map(int, input().split())

    print(f(n, k))

def f(N, K):
    if N == 1 or N == 2:
       return 1
    else:
        f1 = f2 = f3 = 1
        for i in range(3, N-1):
            f3 = f1 + K * f2
            f1, f2 = f2, f3
        return f2

if __name__ == "__main__":
    main()