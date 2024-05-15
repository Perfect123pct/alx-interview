#!/usr/bin/python3

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def isWinner(x, nums):
    """Determine the winner of the Prime Game."""
    def play_game(n):
        """Play a single round of the game."""
        numbers = list(range(1, n + 1))
        player = 'Maria'
        while numbers:
            if is_prime(numbers[0]):
                numbers = [num for num in numbers if num % numbers[0] != 0]
            else:
                numbers.pop(0)
            player = 'Ben' if player == 'Maria' else 'Maria'
        return player

    wins = {'Maria': 0, 'Ben': 0}
    for n in nums:
        wins[play_game(n)] += 1

    if wins['Maria'] > wins['Ben']:
        return 'Maria'
    elif wins['Ben'] > wins['Maria']:
        return 'Ben'
    else:
        return None

