from random import sample

def insertion_sort(alist):
    for index in range(1, len(alist)):
        current_value = alist[index]
        position = index
        while position > 0 and current_value < alist[position - 1]:
            alist[position] = alist[position-1]
            position -= 1
        alist[position] = current_value
        
if __name__ == '__main__':
    nums = sample(range(20), k=10)
    print(nums)
    insertion_sort(nums)
    print(nums)


    
