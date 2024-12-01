def makeChange(coins, total):
    """
    Determines the minimum number of coins needed to achieve a given total.
    
    Parameters:
    coins (list): List of integers representing coin denominations.
    total (int): The target total amount.
    
    Returns:
    int: Minimum number of coins needed to achieve the total, or -1 if not possible.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)  # Sort coins in descending order
    coin_count = 0

    for coin in coins:
        if total <= 0:
            break
        # Find how many of this coin we can use
        count = total // coin
        coin_count += count
        total -= count * coin

    return coin_count if total == 0 else -1

