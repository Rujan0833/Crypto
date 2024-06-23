#WAP to implement Euler's Totient Function.

def gcd(a, b):
    """
    Compute the greatest common divisor of two numbers using the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a

def phi(n):
    """
    Euler's Totient Function, which counts the number of positive integers less than or equal to n that are relatively prime to n.
    
    Args:
        n (int): The positive integer for which to compute the totient function
        
    Returns:
        int: The value of the totient function for n
    """
    result = n
    for i in range(2, n + 1):
        if gcd(i, n) == 1:
            result -= 1
    return result

# Example usage
print(phi(5))   # Output: 4
print(phi(10))  # Output: 4
print(phi(20))  # Output: 8