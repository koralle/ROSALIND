import InputMultiGene
import sys
import pandas as pd
from pandas import DataFrame

class TSandTV(object):
    def __init__(self):
        self.__mutationDict = {"Transitions":0, "Transversions":0}
    
    def check_ts_or_tv(self, base1, base2):
        if set(base1+base2) == set("AG") or set(base1+base2) == set("CT"):
            return "Transitions"
        else:
            return "Transversions" # set("AC"), set("AT"), set("GC"), set("GT")

    def ts_and_tv(self, string1, string2):
        for i in range(0, len(string1)):
            if string1[i] != string2[i]:
                self.__mutationDict[self.check_ts_or_tv(string1[i], string2[i])] += 1
            else:
                pass

        return self.__mutationDict["Transitions"] / self.__mutationDict["Transversions"]
            


def main():
    gene_dict = InputMultiGene.InputMultiGene().input_multi_gene(sys.argv[1])
    gene_name_list = []
    for name in gene_dict.keys():
        gene_name_list.append(name)
    
    print(TSandTV().ts_and_tv(gene_dict[gene_name_list[0]], gene_dict[gene_name_list[1]]))
    

    
    

    


if __name__ == "__main__":
    main()