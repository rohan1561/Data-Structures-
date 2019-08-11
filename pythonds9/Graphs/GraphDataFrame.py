import pandas as pd

class Graph:
    def __init__(self):
        self.columns = []
        self.indices = []
        self.vertlist = pd.DataFrame(columns=self.columns,\
                index=self.indices)

    def add_vertex(self, key):
        self.columns.append(key)
        self.indices.append(key)
        self.vertlist = pd.DataFrame(columns=self.columns,\
                index=self.indices)

    def add_edge(self, f, t, cost=0):
        index_t = self.vertlist.columns.tolist().index(t)
        self.vertlist[f][index_t] = cost

    def get_vertices(self):
        return self.vertlist

if __name__ == '__main__':
    G = Graph()
    for i in range(65, 72):
        G.add_vertex(chr(i))
    print(G.vertlist)
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    G.add_edge('A', 'B', 30)
    G.add_edge('C', 'D', 30)
    print(G.vertlist)
    G.add_vertex('rohan')
    G.add_edge('rohan', 'D', 40)
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    print(G.vertlist)
 
