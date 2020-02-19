
def rev_num(num, n=-1):
    if abs(n) == len(num):
        return num[n]
    return int(str(num[n]) + str(rev_num(num, n-1) ))

print(rev_num(input()))