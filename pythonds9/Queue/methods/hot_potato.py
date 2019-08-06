from ..Queue import Queue
import random

def hot_potato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while len(simqueue) > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        v = simqueue.dequeue()

    return simqueue.dequeue()


if __name__ == '__main__':
    print(hot_potato(list('rohansharma'), 5))

    for n in range(10):
        num = random.randrange(20)
        print(hot_potato(list('rohansharma'), num))

