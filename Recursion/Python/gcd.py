def gcd(a, b):
    return gcd(b, a%b) if b else a


print(gcd(66666666666666666666, 666666666666))