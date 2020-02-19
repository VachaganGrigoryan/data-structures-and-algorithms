def hanoi(diskN, first, second):
    if diskN == 1:
        print("Disk 1 from {0} to {1}".format(first, second))
    else:
        tmp = 6 - first - second
        hanoi(diskN-1, first, tmp)
        print("Disk {0} from {1} to {2}".format(diskN, first, second))
        hanoi(diskN-1, tmp, second)

def main():
    hanoi(3, 1, 2)

if __name__ == "__main__":
    main()