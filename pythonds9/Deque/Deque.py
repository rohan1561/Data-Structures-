class Deque:
    def __init__(self, List=[]):
        self.d = []
        self.List = List
        if List:
            for i in List:
                self.add_front(i)

    def is_empty(self):
        return self.d == []

    def remove_front(self):
        return self.d.pop()

    def remove_rear(self):
        return self.d.pop(0)

    def add_front(self, item):
        self.d.append(item)

    def add_rear(self, item):
        self.d.insert(0, item)

    def size(self):
        return len(self.d)
    
    """
    The following implementations are for the workshop
    """
    def __len__(self):
        return self.size()
    
    def __bool__(self):
        return not self.is_empty()
    
    def __repr__(self):
        return 'Deque([' + ', '.join(str(i) for i in self.d) + '])'
    
    def __str__(self):
        if len(self.d) > 20:
            return 'Dequeue ' + ','.join(str(i) for i in self.d[:20]) + '...'
        return 'Dequeue ' + ','.join(str(i) for i in self.d)
    
    def __contains__(self, item):
        return item in self.d

