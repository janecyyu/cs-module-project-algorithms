'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n):
    # Your code here
    if n <= 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    eat_one_cookie_first = eating_cookies(n - 1)
    eat_two_cookies_first = eating_cookies(n - 2)
    eat_three_cookies_first = eating_cookies(n - 3)
    return eat_one_cookie_first + eat_two_cookies_first + eat_three_cookies_first


def eating_cookies(n, cache):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    # check if the answer is in our cache
    elif cache[n] > 0:
        return cache[n]
    else:
        # otherwise, our cache doesn't contain the answer, so we'll use our
        # recursive logic to calculate it, and then save the answer in our
        # cache for future uses
        cache[n] = eating_cookies(
            n-3, cache) + eating_cookies(n-2, cache) + eating_cookies(n-1, cache)
    return cache[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
