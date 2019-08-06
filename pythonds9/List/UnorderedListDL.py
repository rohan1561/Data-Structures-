from .Node import Node
from .UnorderedList import UnorderedList

class UnorderedListDL(UnorderedList):
    def __init__(self):
        UnorderedList.__init__(self)
        self.tail = None

    def add(self, item):
        """Prepend to a linked list"""
        if self.head == None:
            temp = Node(item)
            temp.set_next(self.head)
            self.head = temp
        else:
            temp = Node(item)
            current = self.head
            temp.set_next(current)
            current.set_prev(temp)
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


