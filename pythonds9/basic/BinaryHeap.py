from random import sample


class BinaryHeap():
    def __init__(self):
        self.__heap_list = [0]
        self.__current_size = 0

    def __perc_up(self, i):
        while i // 2 > 0:
            if self.__heap_list[i] < self.__heap_list[i // 2]:
                temp = self.__heap_list[i // 2]
                self.__heap_list[i // 2] = self.__heap_list[i]
                self.__heap_list[i] = temp

            i = i // 2
    
    def insert(self, k):
        self.__heap_list.append(k)
        self.__current_size += 1
        self.__perc_up(self.__current_size)

    def __perc_down(self,i):
        while (i * 2) <= self.__current_size:
            mc = self.__min_child(i)
            if self.__heap_list[i] > self.__heap_list[mc]:
                tmp = self.__heap_list[i]
                self.__heap_list[i] = self.__heap_list[mc]
                self.__heap_list[mc] = tmp
            i = mc

    def __min_child(self, i):
        if i * 2 + 1 > self.__current_size:
            return i * 2
        else:
            if self.__heap_list[i * 2] < self.__heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1
    
    def del_min(self):
        ret_val = self.__heap_list[1]
        self.__heap_list[1] = self.__heap_list[self.__current_size]
        self.__current_size += 1
        self.__heap_list.pop()
        self.__perc_down(1)
        return ret_val

    def build_heap(self, alist):
        i = len(alist) // 2
        self.__current_size = len(alist)
        self.__heap_list = [0] + alist[:] # Making a copy of alist
        while (i>0):
            self.__perc_down(i)
            i -= 1

if __name__ == '__main__':
    nums = sample(range(20), k=10)
    bh = BinaryHeap()
    nums = bh.build_heap(nums)
    print(bh._BinaryHeap__heap_list)


