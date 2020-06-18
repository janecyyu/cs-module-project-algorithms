'''
Input: a List of integers
Returns: a List of integers
'''
import math


def product_of_all_other_numbers(arr):
    # Your code here
    # sum = math.prod(arr)
    # for i in range(len(arr)):
    #     arr[i] = sum / arr[i]
    # return arr

    length = len(arr)
    # create two array
    L = []
    R = []

    left = 1
    # counting from left to the end of array
    for i in range(length):
        L.append(left)
        left *= arr[i]

    right = 1
    # counting from right to the begining of array
    for i in reversed(range(length)):
        R.insert(i, right)
        # update L array
        L[i] = L[i]*right
        right *= arr[i]
    return L

    # ^^^ runtime O(n), nno division


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
           9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
