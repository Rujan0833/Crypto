import random

def gcd(a, b):
    """
    Compute the greatest common divisor of two numbers using the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a

def is_primitive_root(g, n):
    """
    Check if g is a primitive root of n.
    """
    phi_n = n - 1
    roots = set()
    for r in range(1, phi_n):
        roots.add(pow(g, r, n))
    return len(roots) == phi_n

def find_primitive_root(n):
    """
    Find a primitive root of a prime number n.
    """
    for g in range(2, n):
        if gcd(g, n) == 1 and is_primitive_root(g, n):
            return g
    return None

def diffie_hellman_key_exchange(p):
    """
    Perform the Diffie-Hellman Key Exchange Algorithm.
    
    Args:
        p (int): A large prime number
        
    Returns:
        tuple: (g, Alice's private key, Bob's private key, Shared secret key)
    """
    g = find_primitive_root(p)
    if g is None:
        raise ValueError("No primitive root found for p.")
    
    # Alice's private key
    a = random.randint(2, p - 2)
    A = pow(g, a, p)
    
    # Bob's private key
    b = random.randint(2, p - 2)
    B = pow(g, b, p)
    
    # Shared secret key
    Alice_secret = pow(B, a, p)
    Bob_secret = pow(A, b, p)
    
    return g, a, b, Alice_secret

# Example usage
p = 23  # A prime number
g, a, b, shared_secret = diffie_hellman_key_exchange(p)
print(f"Prime number (p): {p}")
print(f"Primitive root (g): {g}")
print(f"Alice's private key (a): {a}")
print(f"Bob's private key (b): {b}")
print(f"Shared secret key: {shared_secret}")