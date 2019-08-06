from Node import Node
from ParChecker import par_checker_new

class Stack:
    """
    The following is the implementation of Stack using the Node data structure
    """
    def __init__(self, List=[]):
        self.head = None
        self.List = List
        if self.List:
            for i in self.List:
                self.push(i)

    def push(self, item):
        """
        This function appends a value to the Stack
        """
        temp = Node(item)
        
        if self.head == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            current = self.head
            prev = None
            while current != None:
                prev = current
                current = current.get_next()
            prev.set_next(temp)
            temp.set_next(current)

    def pop(self):
        """
        This function returns the last element of
        the stack and removes that element also
        """
        if self.head == None:
            return None
        current = self.head
        prev = None
        while current.get_next() != None:
            prev = current
            current = current.get_next()
        value = current.get_data()
        
        # If the length of the stack is 1, then prev == None and 
        # Nonetype has no attribute get_next(). So, return value
        # and set head to None
        if prev == None:
            self.head = None
            return value
        
        # If length of stack > 1, we remove the last element and 
        # connect the rest of the stack
        prev.set_next(current.get_next())
        return value

    def peek(self):
        """
        This functions returns the value of the 
        last element of the Stack
        """
        current = self.head
        while current.get_next() != None:
            current = current.get_next()
        value = current.get_data()
        return value   

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        This function returns the size of the Stack
        """
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
        return count

    # Datamodel methods

    def __len__(self):
        return self.size()

    def __bool__(self):
        return not self.is_empty()

    def __repr__(self):
        current = self.head
        answer = ''
        while current.get_next() != None:
            answer += f'{current.get_data()},'
            current = current.get_next()

        return 'Stack([' + answer + '])'

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
            return 'Stack ' + ','.join(str(i) for i in answer[:20]) + ' ...'

        return 'Stack ' + ','.join(str(i) for i in answer) 

if __name__ == '__main__':
    print(par_checker_new('<{{[[()]]}}>'))
    print(par_checker_new('{{[[()]]}]'))

