from .Node import Node

class DNode(Node):
    def __init__(self, data):
        Node.__init__(self, data)
        self.next = None
        self.prev = None

    def set_prev(self, item):
        self.prev = item

    def get_prev(self):
        return self.prev


if __name__ == '__main__':
    test = DNode(24)
    print(test.get_data())

