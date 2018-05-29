import networkx as nx
import sys
import re

class InputFormatToEL():
    def __init__(self):
        self.edgeList = []
        self.edgeList_format = ""
        self.header = ""

    def input_edge_list(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            self.edgeList = file.readlines()
            del self.edgeList[0]
            
            for line in self.edgeList:
                self.edgeList_format += line

        with open("EF_"+filename, "w", encoding="utf-8") as file:
            file.write(self.edgeList_format)

            

        G = nx.read_edgelist("EF_"+filename, nodetype=int)
        return list(G)
            
        
def main():
   print( InputFormatToEL().input_edge_list(sys.argv[1]) )


if __name__ == "__main__":
    main()