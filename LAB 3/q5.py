import random

def gcd(a, b):
    """
    Compute the greatest common divisor of two numbers using the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    """
    Compute the greatest common divisor and the Bezout coefficients of two numbers using the Extended Euclidean algorithm.
    
    Returns:
        tuple: (gcd, x, y) where gcd is the greatest common divisor of a and b, and x and y are the Bezout coefficients (satisfying ax + by = gcd).
    """
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b:
        q, r = divmod(a, b)
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
        a, b = b, r
    return a, x0, y0

def modinv(a, m):
    """
    Compute the modular inverse of a modulo m using the Extended Euclidean algorithm.
    """
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError(f"{a} has no modular inverse modulo {m}")
    return x % m

def is_prime(n, k=10):
    """
    Miller-Rabin Primality Test to check if a number n is prime.
    
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

def generate_keypair(p, q):
    """
    Generate an RSA key pair (public key and private key) from two prime numbers p and q.
    
    Returns:
        tuple: (public key, private key)
    """
    n = p * q
    phi_n = (p - 1) * (q - 1)
    
    while True:
        e = random.randrange(2, phi_n)
        if gcd(e, phi_n) == 1:
            break
    
    d = modinv(e, phi_n)
    
    return (e, n), (d, n)

def encrypt(plaintext, public_key):
    """
    Encrypt a plaintext message using the RSA public key.
    
    Args:
        plaintext (int): The plaintext message as an integer
        public_key (tuple): The RSA public key (e, n)
        
    Returns:
        int: The ciphertext as an integer
    """
    e, n = public_key
    return pow(plaintext, e, n)

def decrypt(ciphertext, private_key):
    """
    Decrypt a ciphertext using the RSA private key.
    
    Args:
        ciphertext (int): The ciphertext as an integer
        private_key (tuple): The RSA private key (d, n)
        
    Returns:
        int: The plaintext message as an integer
    """
    d, n = private_key
    return pow(ciphertext, d, n)

# Example usage
p = 61
q = 53
print(f"Prime numbers: p = {p}, q = {q}")

public_key, private_key = generate_keypair(p, q)
print(f"Public key: {public_key}")
print(f"Private key: {private_key}")

plaintext = 12345
ciphertext = encrypt(plaintext, public_key)
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")

decrypted_text = decrypt(ciphertext, private_key)
print(f"Decrypted text: {decrypted_text}")