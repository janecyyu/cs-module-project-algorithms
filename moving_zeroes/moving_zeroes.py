'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here
    # res = [0] * len(arr)
    # i = 0
    # for num in arr:
    #     if num != 0:
    #         res[i] = num
    #         i += 1
    # return res
    # ^^^ runtime is O(n)
    for i in range(len(arr)):
        if arr[i] == 0:
            # remove and then append 0
            arr.remove(arr[i])
            arr.append(0)
    return arr
    # ^^^ runtime is O(n) but space O(1)


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
