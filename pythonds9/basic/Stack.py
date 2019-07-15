class Stack:
    def __init__(self, List=[]):
        self.stack = list()
        self.List = List
        if self.List:
            for i in List:
                self.push(i)

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        item = self.stack[-1]
        return item

    def is_empty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)

    """
    Workshop solutions
    """
    def __len__(self):
        return self.size()
    
    def __bool__(self):
        return not self.is_empty()
    
    def __repr__(self):
        return 'Stack([' + ', '.join(str(i) for i in self.stack) +'])' 
        
    def __str__(self):
        if len(self.stack) > 20:
            return 'Stack ' + ', '.join(str(i) for i in self.stack[:20]) + '...'
        return 'Stack ' + ', '.join(str(i) for i in self.stack)
        
    def __contains__(self, item):
        return item in self.stack

