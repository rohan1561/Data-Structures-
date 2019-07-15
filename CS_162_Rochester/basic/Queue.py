class Queue:
    def __init__(self, List=[]):
        self.queue = []
        self.List = List
        if List:
            for i in List:
                self.enqueue(i)

    def is_empty(self):
        return self.queue == []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)
    
    """
    The following implementations are for the workshop
    """
    def __len__(self):
        return self.size()
    
    def __bool__(self):
        return self.is_empty()
    
    def __repr__(self):
        return 'Queue([' + ', '.join(str(i) for i in self.queue) + '])'
    
    def __str__(self):
        if len(self.queue) > 20:
            return 'Queue ' + ', '.join(str(i) for i in self.queue[:20]) + '...'
        return 'Queue ' + ', '.join(str(i) for i in self.queue)
    
    def __contains__(self, item):
        return item in self.queue

