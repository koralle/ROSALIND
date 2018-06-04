import networkx
import InputFormatToEL as iftel
import sys


def main():

    G = iftel.InputFormatToEL().input_edge_list(sys.argv[1])
    DD_list = [0 for i in range(0, len(list(G)))]

    for node in list(G):
        count = 0
        for num in G.neighbors(node):
            count += G.degree(num)
        DD_list[node-1] = count

    with open("result_rosalind_ddeg.txt", "w", encoding="utf-8") as file:
        file.write(' '.join(map(str, DD_list)))

if __name__ == "__main__":
    main()