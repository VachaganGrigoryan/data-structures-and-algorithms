chache = [0, 1]

def fib(n):
    if n <= 1: return n
    if len(chache) == n:
        chache.append(fib(n-1) + fib(n-2))
    return chache[n]

def main():
    for i in range(int(input("Enter FIB(N): "))):
        print("fib({0}) => {1}".format(i, fib(i)))

if __name__ == "__main__":
    main()