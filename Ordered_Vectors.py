"""
1 - We create a function to print the vector, if last position = -1, the vector is empty, otherwise we print every element and your position
2 - We create a function to insert elements in the vector. First, we need to know where to insert the element, and we do this traversing the vector and
compare the value of each element with the value we want insert, if the element is bigger the value, we first relocate all the subsequence elements to
let the position of this element available to the value we want insert. If the value is bigger than last element, we insert the value in last
position + 1. Not forgot to verify first if the vector is full.
3 - Now, we want search some value in the vector. If the element in certainly position is bigger than value, we stop and return -1.
Otherwise, we search in the whole vector and return -1 when i = last position. Using a binary search, we can divide the search in inferior limit
and upper limit and take the mid of two, if the value we want search is smaller the mid, we concentrate only the in the inferior half,
otherwise in upper, and this process follows until we found the value, otherwise return -1.
4 - We want to remove some element, so first the position of itself is need. If position not exist, return -1. Found the position, now we need to
traversing the entire vector to relocate remain positions, it will be like this, starting in found position, the next position receive the previous
and this process is made until the last position receive the previous.
"""

import numpy as np


class OrderedVector:

    def __init__(self, capacity):
        self._capacity = capacity
        self._lastPosition = -1
        self._values = np.empty(self._capacity, dtype=int)

    # O(N)
    def printer(self):
        if self._lastPosition == -1:
            print("Vector is empty!")
        else:
            for i in range(self._lastPosition + 1):
                print(f"Position: {i} - Element: {self._values[i]}")

    def insert(self, value):
        if self._lastPosition == len(self._values) - 1:
            print("The vector is full, max capacity reached!")
        else:
            position = 0
            for i in range(self._lastPosition + 1):
                position = i
                if self._values[i] > value:
                    break
                elif i == self._lastPosition:
                    position += 1

            x = self._lastPosition
            while x >= position:
                self._values[x + 1] = self._values[x]
                x -= 1

            self._values[position] = value
            self._lastPosition += 1

    def search(self, value):
        for i in range(self._lastPosition + 1):
            if self._values[i] > value:
                return -1
            elif self._values[i] == value:
                return i
            elif i == self._lastPosition and self._values[i] < value:
                return -1

    def binary_search(self, value):
        inferior_limit = 0
        upper_limit = self._lastPosition
        while inferior_limit <= upper_limit:
            mid = int((inferior_limit + upper_limit) / 2)
            if self._values[mid] == value:
                return mid
            elif self._values[mid] < value:
                inferior_limit = mid + 1
            elif self._values[mid] > value:
                upper_limit = mid - 1
        return -1

    def remove(self, value):
        position = self.search(value)
        if position == -1:
            return -1
        else:
            for i in range(position, self._lastPosition):
                self._values[i] = self._values[i+1]
            self._lastPosition -= 1


if __name__ == '__main__:
    Vector = OrderedVector(5)

    # Vector.printer()
    Vector.insert(5)
    Vector.insert(10)
    # Vector.printer()
    Vector.insert(1)
    # Vector.printer()
    Vector.insert(8)
    # Vector.printer()
    Vector.insert(15)
    # Vector.printer()
    Vector.printer()
    print("---")
    print(Vector.search(8))
    print("---")
    Vector.remove(5)
    Vector.printer()
    print("---")
    Vector.remove(10)
    Vector.printer()
    print(Vector.remove(5))
    print("---")
    Vector.printer()
    print(Vector.binary_search(8))
    print("---")
    print(Vector.binary_search(16))
