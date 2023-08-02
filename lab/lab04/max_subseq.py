def max_subseq(n, t):
    """
    Return the maximum subsequence of length at most t that can be found in the given number n.
    For example, for n = 20125 and t = 3, we have that the subsequences are
    """
    if t == 0:
        return 0
    elif n < 10:
        return n
    else:
        allbutlast, last = n // 10, n % 10
        use_ones = max_subseq(allbutlast, t-1) *10 +last
        not_use_ones = max_subseq(allbutlast, t)
        return max(use_ones, not_use_ones)





# sequence num order don't need to follow the order of n
#     if t == 0:
#         return 0
#     elif t > len(str(n)):
#         return n
#     else:
#         L = []
#         while n > 0:
#             L.append(n % 10)
#             n = n//10
#         L = sorted(L)
#         maxnum, n = 0, len(L)
#         for i in range(t):
#             maxnum = maxnum * 10 + L[-1]
#             L.pop()
#         return maxnum