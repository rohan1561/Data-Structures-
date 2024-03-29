import random

def sequential_search(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1

    return found


if __name__ == '__main__':
    testlist = random.sample(range(10), 6)
    print(testlist)
    print(sequential_search(testlist, 7))

