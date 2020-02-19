def generateString(abc, i, string):
    if (i == 0):
        print(string)
        return

    for letter in abc:
        appended = letter + string
        generateString(abc, i - 1, appended)

def main():

    abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lenA = len(abc)

    for i in range(1, lenA + 1):
        generateString(abc, i, "")

if __name__ == "__main__":
    main()