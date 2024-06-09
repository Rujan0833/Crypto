#WAP to implement Miller-Rabin Algorithm.


import random

def miller_rabin(n, k=10):
    """
    Miller-Rabin Primality Test
    
    Args:
        n (int): The number to be tested for primality
        k (int): The number of iterations (default=10)
        
    Returns:
        bool: True if n is probably prime, False otherwise
    """
    if n < 2:
        return False
    
    if n <= 3:
        return True
    
    if n % 2 == 0:
        return False
    
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    
    return True

# Example usage
print(miller_rabin(7))  # True
print(miller_rabin(10))  # False
print(miller_rabin(561))  # True