#!/usr/bin/python3
def isWinner(x, nums):
    if x < 1 or not nums:
        return None
    
    max_num = max(nums)
    
    # Sieve of Eratosthenes to find all primes up to max_num
    sieve = [True] * (max_num + 1)
    sieve[0], sieve[1] = False, False  # 0 and 1 are not prime numbers
    p = 2
    while (p * p <= max_num):
        if sieve[p] == True:
            for i in range(p * p, max_num + 1, p):
                sieve[i] = False
        p += 1
    
    # List of primes up to max_num
    primes = [p for p in range(max_num + 1) if sieve[p]]
    
    # Function to play one game
    def play_game(n):
        if n < 2:
            return "Ben"
        nums = list(range(1, n + 1))
        primes_used = [False] * (n + 1)
        current_player = "Maria"
        
        while True:
            move_made = False
            for prime in primes:
                if prime > n:
                    break
                if not primes_used[prime]:
                    move_made = True
                    # Mark this prime and its multiples
                    for multiple in range(prime, n + 1, prime):
                        primes_used[multiple] = True
                    break
            if not move_made:
                break
            current_player = "Ben" if current_player == "Maria" else "Maria"
        
        return "Ben" if current_player == "Maria" else "Maria"
    
    # Play all rounds and count wins
    maria_wins = 0
    ben_wins = 0
    for num in nums:
        winner = play_game(num)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# You can test the function with the following lines:
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

