def next_largest_coin(coin):

    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25
        
def count_coins(total):

    def count_coins_helper(n, m):
        if n == 0:
            return 1
        elif n < 0 :
            return 0
        elif m == 0:
            return 0
        else:
            next_coin = next_largest_coin(m)
            with_smallest = count_coins_helper(n-m, m)
            without_smallest = count_coins_helper(n, next_coin)
            return with_smallest + without_smallest

    return count_coins_helper(total, 1)
    