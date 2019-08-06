from random import sample

def quick_sort(alist):
    if len(alist) <= 1:
        return alist
    pivot = alist[0]

    left = 1
    right = len(alist) - 1
    while left <= right:
        if alist[left] > pivot:
            if alist[right] < pivot:
                alist[left], alist[right] = alist[right], alist[left]
                left += 1
                continue
            right -= 1
            continue
        left += 1
    alist[right], alist[0] = alist[0], alist[right]

    answer = quick_sort(alist[:right]) + [alist[right]] +\
            quick_sort(alist[right + 1:])

    return answer

if __name__ == '__main__':
    nums = sample(range(20), k=10)
    print(quick_sort(nums))

