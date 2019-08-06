import string

print(string.ascii_uppercase)
print(string.digits)
def to_str(n, base):
    convert_string = string.digits + string.ascii_uppercase[0:6]
    if n < base:
        return convert_string[n]
    else:
        return to_str(n//base) + convert_string(n % base)

print(to_str(34, 10))

