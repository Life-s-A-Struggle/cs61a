HW_SOURCE_FILE=__file__


def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    if x < 8:
        return 0
    else:
        all_but_last, last = x // 10, x % 10
        if last == 8:
            return num_eights(all_but_last) + 1 
        else:
            return num_eights(all_but_last)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    def pingpong_helper(index, dir, result):
        if index == n:
            return result
        else:
            if index % 8 == 0 or num_eights(index):
                return pingpong_helper(index + 1, -dir, result - dir) #when if_ = True, dir will maintain it's value till next loop.(8+1,-1,8-1)
            else:
                return pingpong_helper(index + 1, dir, result + dir)
    return pingpong_helper(index = 1, dir = 1, result = 1)


# # Alternate Solution

# return helper(n, 1, 1, 1)

# def helper(n, i, curr, direction):
#     if i == n:
#         return curr
#     else:
#         if i % 7 == 0 or has_seven(i):
#             return helper(n, i + 1, curr - direction, -direction)
#         else:
#             return helper(n, i + 1, curr + direction, direction)


# # iteration

# def pingpong(n):
#     i, curr, direction = 1, 1, 1
#     while i < n:
#         if i % 7 == 0 or has_seven(i):
#             direction = -direction
#         curr += direction
#         i += 1
#     return curr
