from BinaryHeap import BinaryHeap

class PriorityQueue(BinaryHeap):
    def __init__(self, maxlength):
        super().__init__()
        self.max = maxlength
    
    def check_priority(self):
        """
        This function checks if the priorities
        are of int type or not
        """
        pri = list(map(lambda x: isinstance(x[0], int), self.heap_list[1:]))
        if sum(pri) == self.current_size:
            return True
        else:
            return 'Please use integers to set priorities of values'

    def perc_up(self, i):
        """
        Perc up the tuple i according to its rank.
        Ranks are the first elements of the tuples.

        Parameters
        ----------
        i: Python tuple type to be percolated up

        Returns
        -------
        None
        """
        # Check if the priorities are integers first!
        if self.check_priority():
            while i//2 > 0:
                if self.heap_list[i][0] < self.heap_list[i//2][0]:
                    self.heap_list[i//2], self.heap_list[i] =\
                            self.heap_list[i], self.heap_list[i//2]
                i = i // 2
 
    def perc_down(self,i):
        """
        Perc down the tuple i according to its rank.
        Ranks are the first elements of the tuples.

        Parameters
        ----------
        i: Python tuple type to be percolated down

        Returns
        -------
        None
        """
        if self.check_priority():
            while (i * 2) <= self.current_size:
                mc = self.min_child(i)
                # Used >= and not > because values added later will go lower
                # making sure that values added later are also removed later
                if self.heap_list[i][0] >= self.heap_list[mc][0]:
                    self.heap_list[i], self.heap_list[mc] =\
                            self.heap_list[mc], self.heap_list[i]
                i = mc

    def min_child(self, i):
        # Same as the parent class method except this one checks for the 
        # Priority number instead of the number itself
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2][0] < self.heap_list[i * 2 + 1][0]:
                return i * 2
            else:
                return i * 2 + 1

    def maintain_size(self):
        """
        This function makes sure that the size of the queue is limited to 
        the maximum size
        """
        while self.current_size > self.max:
            self.del_max()
            self.current_size -= 1

    def del_max(self):
        """
        This function deletes the element with the least priority
        """

        # Get the index of the element with the least priority
        # .index method returns the smallest index of the value in the list
        # which is ideal since we first need to drop the element we added first
        # in case where there are multiple least priority elements (same rank)
        least_index = self.heap_list.index(sorted(self.heap_list[1:],
                                                key=lambda x: x[0])[-1])

        # Exchange the least priority element with the last element
        # Remove the least priority element. Perc up the element in place
        # of it.
        self.heap_list[least_index], self.heap_list[-1] = \
            self.heap_list[-1], self.heap_list[least_index]
        self.perc_up(least_index)
        self.heap_list.pop()

    def enqueue(self, tup):
        super().insert(tup)
        self.current_size += 1
        self.maintain_size()

    def dequeue(self):
        """
        This function returns the element with the maximum priority
        """
        # Note that if multiple elements have the same priority, the one
        # added first will come before. perc_down has been changed accordingly
        # So super().del_min() works!
        try:
            value = super().del_min()
            self.current_size -= 1
            return value
        except:
            raise IndexError('Queue Empty')

    def build_heap(self, alist):
        super().build_heap(alist)
        self.maintain_size()

if __name__ == '__main__':
    from random import sample
    nums = sample(range(20), k=20)
    ranks = list(range(20))
    values = list(zip(ranks, nums))
    print(values)
    bh = PriorityQueue(15)
    bh.build_heap(values)
    print(bh.heap_list)

