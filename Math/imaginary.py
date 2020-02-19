def imaginary(x):
    img = [1, 'i', -1, "-i"]
    print("I^({0}) => {1}".format(x, img[x%4]))
    # return img[x%4]

imaginary(100)
imaginary(501)
imaginary(7321)
imaginary(99)
imaginary(38)
imaginary(101)