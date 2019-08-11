from random import sample

class BinaryHeap():
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def perc_up(self, i):
        while i//2 > 0:
            if self.heap_list[i] < self.heap_list[i//2]:
                self.heap_list[i//2], self.heap_list[i] =\
                        self.heap_list[i], self.heap_list[i//2]
            i = i // 2
    
    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.perc_up(self.current_size)

    def perc_down(self,i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] =\
                        self.heap_list[mc], self.heap_list[i]
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1
    
    def del_min(self):
        ret_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size += 1
        self.heap_list.pop()
        self.perc_down(1)
        return ret_val

    def build_heap(self, alist):
        i = len(alist) // 2
        self.current_size = len(alist)
        self.heap_list = [0] + alist[:] # Making a copy of alist
        while (i>0):
            self.perc_down(i)
            i -= 1

if __name__ == '__main__':
    from Visualizer import viz_graph_bh
    import time
    nums = sample(range(20), k=10)
    bh = BinaryHeap()
    bh.build_heap(nums)

    viz = viz_graph_bh(bh.heap_list)
    viz.view()
    print('xxxxxxxxxxx')
    time.sleep(10)

    bh.del_min()
    viz = viz_graph_bh(bh.heap_list)
    viz.view()


