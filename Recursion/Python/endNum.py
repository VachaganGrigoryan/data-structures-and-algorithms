def Xx2(end, k = -1):
    return  (end, 2*int(end)) if int(end[-1:]+end[:-1]) == int(end)*2 else Xx2(str(int(end[k:])*2) + end[-1:], k-1)

if __name__ == "__main__":
    print(Xx2(input("Enter end : ")))