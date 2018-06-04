import math
import itertools

def main():
    num = int(input())
    num_list = [i for i in range(1, num+1)]
    
    with open('result_permutation.txt', "w", encoding="utf-8") as file:
        file.write(str(math.factorial(num)) + '\n')
        for v in itertools.permutations(num_list):
            file.write( ' '.join(list(map(str, v))) + '\n')

if __name__ == "__main__":
    main()