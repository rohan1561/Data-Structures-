import sys
def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number-1)

def fibonacci(num):
    a = 0
    b = 1
    count = 0
    while count < num:
        c = a + b
        a = b
        b = c
        count += 1
    return c

def fib_rec(num):
    if num < 2:
        return 1
    return fib_rec(num-1) + fib_rec(num-2)

print('factorial of 5: ', factorial(4))
print('fibonacci of 4:', fibonacci(4))
print('fibonacci of 4:', fib_rec(4))
print(sys.getrecursionlimit())
sys.setrecursionlimit(4000)
print(sys.getrecursionlimit())

