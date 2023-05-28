from abc import ABC, abstractmethod
from typing import List


class BaseSort:

    def __init__(self, array: List):
        self._array = array

    @abstractmethod
    def sort(self):
        ...


class BubbleSort(BaseSort):

    def sort(self):
        for i in range(len(self._array)):
            swapped = False
            for j in range(len(self._array) - i - 1):
                if self._array[j] > self._array[j + 1]:
                    self._array[j], self._array[j + 1] = self._array[j + 1], self._array[j]
                    swapped = True

            if not swapped:
                break


class SelectionSort(BaseSort):

    def sort(self):
        for select in range(len(self._array)):
            min_idx = select

            for i in range(select + 1, len(self._array)):
                if self._array[i] < self._array[min_idx]:
                    min_idx = i

            self._array[select], self._array[min_idx] = self._array[min_idx], self._array[select]


class InsertionSort(BaseSort):

    def sort(self):
        for i in range(1, len(self._array)):
            key = self._array[i]

            j = i - 1
            while j >= 0 and key < self._array[j]:
                self._array[j + 1] = self._array[j]
                j -= 1

            self._array[j + 1] = key


class MergeSort(BaseSort):

    def sort(self):
        if len(self._array) > 1:
            mid = len(self._array) // 2
            left = self._array[:mid]
            right = self._array[mid:]

            MergeSort(array=left).sort()
            MergeSort(array=right).sort()

            l_idx = r_idx = a_idx = 0

            while l_idx < len(left) and r_idx < len(right):
                if left[l_idx] < right[r_idx]:
                    self._array[a_idx] = left[l_idx]
                    l_idx += 1
                else:
                    self._array[a_idx] = right[r_idx]
                    r_idx += 1
                a_idx += 1

            while l_idx < len(left):
                self._array[a_idx] = left[l_idx]
                l_idx += 1
                a_idx += 1

            while r_idx < len(right):
                self._array[a_idx] = right[r_idx]
                r_idx += 1
                a_idx += 1


class QuickSort(BaseSort):

    def sort(self):
        self._quick_sort(0, len(self._array) - 1)

    def _quick_sort(self, low, high):
        if low < high:
            pi = self._partition(low, high)

            self._quick_sort(low, pi - 1)

            self._quick_sort(pi + 1, high)

    def _partition(self, low, high):
        pivot = self._array[high]

        i = low - 1

        for j in range(low, high):
            if self._array[j] <= pivot:
                i += 1

                self._array[i], self._array[j] = self._array[j], self._array[i]

        self._array[i + 1], self._array[high] = self._array[high], self._array[i + 1]

        return i + 1


class CountingSort(BaseSort):

    def sort(self):
        size = len(self._array)
        output = [0] * size

        c_len = max(self._array) + 1
        min_elm = min(self._array)
        if min_elm < 0:
            c_len += abs(min_elm)

        count = [0] * c_len

        for i in range(size):
            count[self._array[i] - min_elm] += 1

        for i in range(1, c_len):
            count[i] += count[i - 1]

        i = size - 1
        while i >= 0:
            output[count[self._array[i] - min_elm] - 1] = self._array[i]
            count[self._array[i] - min_elm] -= 1
            i -= 1

        for i in range(0, size):
            self._array[i] = output[i]

    def _sort(self):
        size = len(self._array)

        c_len = max(self._array) + 1
        min_elm = min(self._array)
        if min_elm < 0:
            c_len += abs(min_elm)

        count: List[int] = [None] * c_len

        for i in range(size):
            idx = self._array[i] - min_elm
            if count[idx] is None:
                count[idx] = 1
            else:
                count[idx] += 1

        i = 0
        for value, count in enumerate(count):
            if isinstance(count, int):
                self._array[i:i+count] = [value - -min_elm] * count
                i += count


if __name__ == '__main__':
    data = [-2, 45, 0, 11, -9]
    # data = [4, 2, 2, 8, 3, 3, 1]

    CountingSort(data)._sort()

    print(data)
