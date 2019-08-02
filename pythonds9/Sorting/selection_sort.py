import random
def selection_sort(alist):
    for fill_slot in range(len(alist)-1, 0, -1):
        pos_of_max = 0
        for location in range(1, fill_slot+1):
            if alist[location] > alist[pos_of_max]:
                pos_of_max = location

        alist[fill_slot], alist[pos_of_max] =\
                alist[pos_of_max], alist[fill_slot]



if __name__ == '__main__':
    alist = [random.randrange(10) for i in range(6)]
    print('before sorting')
    print(alist)
    selection_sort(alist)
    print('after sorting')
    print(alist)

