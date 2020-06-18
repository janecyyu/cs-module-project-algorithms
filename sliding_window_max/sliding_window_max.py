'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(numbers, k):
    def get_window_max(start_idx):
        window_max = float('-inf')
        for i in range(start_idx, start_idx + k):
            window_max = max(window_max, numbers[i])
        return window_max

    res = []

    for i in range(len(numbers) - k + 1):
        window_max = get_window_max(i)
        res.append(window_max)

    return res


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
