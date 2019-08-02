from random import sample

def merge(list1, list2):

    i = 0
    j = 0
    fulllist = []

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            fulllist.append(list1[i])
            i += 1
        else:
            fulllist.append(list2[j])
            j += 1

    fulllist += list2[j:]
    fulllist += list1[i:]

    return fulllist


def merge_sort(alist):
    print('splitting')
    if len(alist) == 1:
        return alist

    else:
        mid = len(alist) // 2
        left_half = alist[:mid]
        right_half = alist[mid:]
        left_half = merge_sort(left_half)
        right_half = merge_sort(right_half)
        final = merge(left_half, right_half)
    return final


if __name__ == '__main__':
    nums = sample(range(20), k=10)
    print(nums)
    print(merge_sort(nums))

