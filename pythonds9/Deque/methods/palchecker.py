from ..Deque import Deque

def palchecker(string):
    chars = Deque()
    for s in string:
        chars.add_rear(s)

    check = True
    while chars.size() > 1 and check:
        first = chars.remove_front()
        last = chars.remove_rear()

        if first != last:
            check = False

    return check

