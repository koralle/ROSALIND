def main():
    """
    部分集合の数はnCrをr=0->nまで足した和になる。
    ex.n = 3) 3C0 + 3C1 + 3C2 + 3C3
    これは二項定理で2のn乗に等しくなる 
    """

    num = int(input())
    print(2 ** num)
    
if __name__ == "__main__":
    main()