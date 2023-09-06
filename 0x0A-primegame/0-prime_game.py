def isWinner(x, nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def can_win(n):
        # Generate a list of booleans where prime[i] is True if i is prime
        prime = [False, False] + [True] * (n - 1)

        for p in range(2, int(n**0.5) + 1):
            if prime[p]:
                for i in range(p * p, n + 1, p):
                    prime[i] = False

        return sum(prime) % 2 != 0  # True if the number of primes is odd

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if can_win(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
