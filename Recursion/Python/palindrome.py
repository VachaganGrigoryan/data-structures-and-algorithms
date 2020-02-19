def palindrom(st, n=0):
    if n==len(st)//2:
        return True
    if st[n] != st[-1-n]:
        return False
    return palindrom(st, n+1)

print(palindrom(input("Enter any string : ")))