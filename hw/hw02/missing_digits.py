def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    def count_missing_digits(n, curr):
        if n < 10:
            return 0
        last= n % 10
        pre = n //10 % 10
        if pre == last: # check whether pre equal last or not, if true then n//10
            n = n // 10
            return count_missing_digits(n, n%10)
        else:
            if pre< curr <last: 
                return count_missing_digits(n, curr-1) +1
            elif curr == pre: #till curr decrease to pre, then n//10, check another digit between pre and pre-pre
                return count_missing_digits(n//10, curr-1)
            else:
                return count_missing_digits(n, curr-1)
    return count_missing_digits(n, n%10-1)


#  PKUflying
#     all_but_last, last = n // 10, n % 10
#     if all_but_last == 0:
#         return 0
#     last_last = all_but_last % 10
#     miss = 0 if last - last_last <= 1 else last - 1 - last_last
#     return missing_digits(all_but_last) + miss

# # Altrenate Solution 2
#     def missing_digits_helper(n, k, result=0):
#         if n == 0:
#             return result
#         else:
#             all_but_last, last = n // 10, n % 10
#             if k - last > 1:
#                 return missing_digits_helper(all_but_last, last, result + (k - last -1))
#             else:
#                 return missing_digits_helper(all_but_last, last, result)

#     return missing_digits_helper(n, n%10)