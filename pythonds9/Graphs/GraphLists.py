from Vertex import Vertex

class Graph:
    def __init__(self):
        self.vertlist = []
        self.num_vertices = 0

    def __iter__(self):
        keys = list(map(lambda x: x[0].get_id(), self.vertlist))
        return iter(keys)

    def __contains__(self):
        keys = list(map(lambda x: x[0].get_id(), self.vertlist))
        return n in vertlist

    def add_vertex(self, key):
        keys = list(map(lambda x: x[0].get_id(), self.vertlist))
        if key not in keys:
            self.num_vertices += 1
            new_vertex = Vertex(key)
            for k in self.vertlist:
                k[1].append('')
            self.vertlist.append([new_vertex, ['']*self.num_vertices])

    def get_vertex(self, n):
        for i in self.vertlist:
            if i[0].get_id() == n:
                return i[1]
        else:
            return None

    def add_edge(self, f, t, cost=0):
        keys = list(map(lambda x: x[0].get_id(), self.vertlist))
        if f not in keys:
            raise VertexError(f'Vertex key {f} not found')
        if t not in keys:
            raise VertexError(f'Vertex key {t} not found')
        index1 = keys.index(f)
        index2 = keys.index(t)

        self.vertlist[index1][1][index2] = cost
        self.vertlist[index2][1][index1] = cost

    def get_vertices(self):
        return self.vertlist

if __name__ == '__main__':
    from Vertex import Vertex
    from VertexError import VertexError
    from Visualizer import viz_graph
    import matplotlib.pyplot as plt

    G = Graph()
    for i in range(65, 72):
        G.add_vertex(chr(i))
    for i in G.vertlist:
        print(i)
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    G.add_edge('A', 'B', 30)
    G.add_edge('C', 'D', 30)
    for i in G.vertlist:
        print(i)
    G.add_vertex('rohan')
    G.add_edge('rohan', 'D', 40)
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    for i in G.vertlist:
        print(i)
 
