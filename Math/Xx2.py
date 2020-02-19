def Xx2(end):
    n, k = end, -1
    while int(n[-1:]+n[:-1]) != int(n)*2:
        n, k = str(int(n[k:])*2) + end, k - 1
    return n, 2*int(n)

if __name__ == "__main__":
    print(Xx2(input("Enter end : ")))