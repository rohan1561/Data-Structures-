import random
from math import log2
def bin_search(alist, item):
    global count
    count += 1
    mid = len(alist)//2
    if item > alist[-1]:
        return False
    elif item == alist[mid]:
        return True
    elif len(alist) == 0:
        return False
    elif item < alist[mid]:
        return bin_search(alist[:mid], item)
    else:
        return bin_search(alist[mid:], item)

if __name__ == '__main__':
    item = random.randrange(60)
    sample = sorted(random.sample(range(100), 60))
    print(f'{item} is to be searched')
    print('list is')
    print(sample)
    count = 0
    print(bin_search(sample, item))
    print(f'number of steps taken {count}')
    print(f'upper bound of the number of steps = {log2(60)}')

