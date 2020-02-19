c = 0


def generateArray(abc, m, word):
    global c
    if m == 0:
        print(word)
        c += 1
        return

    for leter in abc:
        newWord = [leter] + word
        generateArray(abc, m-1, newWord)


def main():

    # abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    abc = "abcdefg"
    lenA = len(abc)

    for i in range(1, lenA + 1):
        generateArray(abc, i, [])

    SUM = [lenA**i for i in range(1, lenA+1)]
    print(c, sum(SUM), SUM)


if __name__ == "__main__":
    main()
