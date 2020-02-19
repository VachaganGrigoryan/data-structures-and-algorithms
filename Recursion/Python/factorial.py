cache = [1]


def fact(n):
    if len(cache) == n:
        cache.append(n * fact(n-1))
    return cache[n]


for i in range(int(input("Enter n: "))):
    print("{0} => {1}".format(i, fact(i)))
