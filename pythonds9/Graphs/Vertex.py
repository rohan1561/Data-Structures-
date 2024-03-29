import sys

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}
        self.color = 'white'
        self.dist = sys.maxsize
        self.pred = None
        self.disc = 0
        self.fin = 0

    def __str__(self):
        return str(self.id) + 'connected to' + str([x.id for x in\
                self.connected_to])

    def add_neighbor(self, nbr, weight=0):
        self.connected_to[nbr] = weight

    def set_color(self, color):
        self.color = color

    def set_distance(self, distance):
        self.distance = distance

    def set_pred(self, p):
        self.pred = p

    def set_discovery(self, dtime):
        self.disc = dtime

    def set_finish(self, ftime):
        return self.fin

    def get_discovery(self):
        return self.disc

    def get_finish(self):
        return self.fin

    def get_pred(self):
        return self.pred

    def get_dist(self):
        return self.dist
    
    def get_color(self):
        return self.color

    def get_weight(self, nbr):
        return self.connected_to[nbr]

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connected_to[nbr]
