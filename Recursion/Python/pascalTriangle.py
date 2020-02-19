cache = [1]


def fact(n):
    if len(cache) == n:
        cache.append(n * fact(n-1))
    return cache[n]


def pascal(n):
    return [[fact(i)//(fact(j)*fact(i-j)) for j in range(i+1)] for i in range(n)]


n = int(input("Enter n: "))

pas = pascal(n)
for i in range(n):
    print(' '*(n - i), pas[i])

# for i in range(10000):
#     print(fact(i))
