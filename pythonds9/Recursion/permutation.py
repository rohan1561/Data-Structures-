def permutation(s, prefix=""):
    count = 0
    count += 1
    n = len(s)
    if n == 0:
        pass
    else:
        for i in range(n):
            permutation(s[0:i] + s[i+1:n], prefix + s[i])

print(permutation('test'))

