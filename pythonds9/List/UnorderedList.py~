from Node import Node


class UnorderedList:
    def __init__(self, List=[]):
        self.head = None
        self.List = List
        if self.List:
            for i in List:
                self.add(i)

    def is_empty(self):
        """Return if the linked list is empty"""
        return self.head == None

    def add(self, item):
        """Prepend to a linked list"""
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def length(self):
        """Return the length of a linked list"""
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        """Returns: bool. If an element is present or not"""
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self.head
        found = False
        previous = None
        while current != None and not found:
            if current.get_data() == item:
                found = True
                previous.set_next(current.get_next())
            else:
                previous = current
                current = current.get_next()
        if previous == None and found:
            self.head = current.get_next()
            
    """
    The following implementations are for the workshop
    """
    def __len__(self):
        return self.length()
    
    def __bool__(self):
        return not self.is_empty()
    
    def __repr__(self):
        current = self.head
        answer = ''
        while current.get_next() != None:
            answer += f'{current.get_data()},'
            current = current.get_next()
            
        return 'UnorderedList([' + answer + '])'
    
    def __str__(self):
        answer = []
        size = 0
        current = self.head
        while current != None:
            answer.append(current.get_data())
            current = current.get_next()
            size += 1
            if size > 20:
                break
        
        if size > 20:
            return 'UO-List ' + '->'.join(str(i) for i in answer[:20]) + ' ...'
        
        return 'UO-List ' + '->'.join(str(i) for i in answer)
    
    def __contains__(self, item):
        return self.search(item)

