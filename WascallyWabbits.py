dict = {}

def main():
    n, k = map(int, input().split())

    print(f(n, k))
    

def f(N, K):
    """if N == 1 or N == 2:
        return 1
    else:
        return f(N-1, K) + K * f(N-2, K)"""
        
    
    
    if N == 1 or N == 2:
        dict[N] = 1
        return dict[N]

    else:
        if N in dict.keys():
            return dict[N]
        else:
            dict[N] = f(N-1, K) + 3 * f(N-2, K)
            return dict[N]



if __name__ == "__main__":
    main()