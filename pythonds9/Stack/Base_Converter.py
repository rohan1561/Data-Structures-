from Stack import Stack

def bin_converter(number):
    remstack = Stack()
    while number > 0:
        rem = number % 2
        remstack.push(rem)
        number = number//2

    bin_string = ''
    while not remstack.is_empty():
        bin_string += str(remstack.pop())

    return '0b'+bin_string

print(bin(32))
print(bin_converter(32))


def base_converter(number, base):
    strings = '0123456789ABCDEF'
    remstack = Stack()
    while number > 0:
        rem = number % base
        remstack.push(rem)
        number = number // base
    answer = ''
    while not remstack.is_empty():
        answer += strings[remstack.pop()]

    return answer

print(base_converter(3200, 16))

