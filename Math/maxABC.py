arr = [int(v) for v in input("Enter ARRAY ::: ").split()]
b= arr[0]
for a in arr[1:]:
    b = (a+b - abs(a-b))//2 + abs(a-b)

print(b)

for a in arr[1:]:
    dif = abs(a-arr[0])
    arr[0] = (a+arr[0] - dif)//2 + dif
print(arr[0])