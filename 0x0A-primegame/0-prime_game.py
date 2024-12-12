def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.

    Args:
        x (int): The number of rounds.
        nums (list): List of integers representing the upper bounds for each round.

    Returns:
        str: The name of the player that won the most rounds, or None if it's a tie.
    """
    if not nums or x < 1:
        return None

    # Helper function to generate a sieve of primes up to the maximum number in nums
    def sieve(n):
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        return is_prime

    # Determine the largest number in nums for the sieve
    max_num = max(nums)
    primes = sieve(max_num)

    # Precompute the number of primes up to each number
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Number of primes up to n
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage
if __name__ == "__main__":
    print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))

