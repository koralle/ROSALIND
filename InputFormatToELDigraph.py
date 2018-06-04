import networkx as nx
import sys
import re
import matplotlib.pyplot as plt

class InputFormatToEL():
    def __init__(self):
        self.edgeList = []
        self.edgeList_format = ""
        self.header = ""
        self.G = nx.DiGraph()

    def input_edge_list(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            self.edgeList = file.readlines()
            self.data = self.edgeList[0].split()
            [self.G.add_node(num) for num in range(1, int(self.data[0])+1)]
            for line in range(1, int(self.data[1])+1):
                tmp = self.edgeList[line].split()
                self.G.add_edge(int(tmp[0]), int(tmp[1]))

        return self.G
        """with open(filename, "r", encoding="utf-8") as file:
            self.edgeList = file.readlines()
            del self.edgeList[0]
            
            for line in self.edgeList:
                self.edgeList_format += line

        with open("EF_"+filename, "w", encoding="utf-8") as file:
            file.write(self.edgeList_format)"""
            
        
def main():
     DiGraph = InputFormatToEL().input_edge_list(sys.argv[1])
     nx.draw_networkx(DiGraph)
     plt.show()


if __name__ == "__main__":
    main()