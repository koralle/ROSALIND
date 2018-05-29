import sys
import InputFormatToEL as iftel
import networkx as nx
import re

class DegreeArray():

    def __init__(self):
        self.G = nx.Graph()
        self.NodeList = []
        self.result = []
        self.output = []

    def degree_array(self, filename):
        iftel.InputFormatToEL().input_edge_list(sys.argv[1])
        with open('EF_'+filename, 'r', encoding='utf-8') as file:
            for line in file:
                if '\n' in line:
                    line = re.sub('\n', '', line)
                line = line.split()
                line = [int(num) for num in line]
                self.G.add_edge(line[0], line[1])

        self.degree_list = list(self.G.degree(self.G.nodes()))
        for item in self.degree_list:
            item = list(tuple(item))
            self.result.append(item)
        
        self.result = self.list_sort(self.result)
        
        for List in self.result:
            self.output.append( str(List[1]) )


        # print( ' '.join(self.output) )
        with open("output_for_rosalind_deg.txt", "w", encoding="utf-8") as file:
            file.write(' '.join(self.output)) 

    def list_sort(self, list_list):
        for i in range(len(list_list)):
            for j in range(len(list_list)-1, i, -1):
                if list_list[j][0] < list_list[j-1][0]:
                    list_list[j], list_list[j-1] = list_list[j-1], list_list[j]
            
        return list_list
            
        
        

    

def main():
    DegreeArray().degree_array(sys.argv[1])
    

if __name__ == "__main__":
    main()