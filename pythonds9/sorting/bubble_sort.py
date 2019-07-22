import random
def bubble_sort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]


def short_bubble_sort(alist):
    exchanges = True
    pass_num = len(alist) - 1
    while pass_num > 0 and exchanges:
        exchanges = False
        print(f'pass{len(alist) - pass_num}')
        for i in range(pass_num):
            if alist[i] > alist[i+1]:
                exchanges = True
                alist[i], alist[i+1] = alist[i+1], alist[i]
        pass_num -= 1

alist = [random.randrange(10) for i in range(5)]
print(alist)
bubble_sort(alist)
print(alist)

print('xxxxxxxxxxxxx')
blist = [random.randrange(10) for i in range(5)]
print(blist)
print('short bubble sort')
short_bubble_sort(blist)
print(blist)


