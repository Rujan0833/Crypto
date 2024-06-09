import random

def gcd(a, b):
    """
    Compute the greatest common divisor of two numbers using the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a

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

def find_primitive_root(p):
    """
    Find a primitive root of a prime number p.
    """
    if not is_prime(p):
        raise ValueError(f"{p} is not a prime number")
    
    for g in range(2, p):
        if pow(g, p - 1, p) == 1:
            continue
        powers = set()
        for r in range(1, p):
            powers.add(pow(g, r, p))
        if len(powers) == p - 1:
            return g
    
    return None

def generate_key_pair(p, g):
    """
    Generate an ElGamal key pair (public key and private key).
    
    Args:
        p (int): A large prime number
        g (int): A primitive root modulo p
        
    Returns:
        tuple: (public key, private key)
    """
    private_key = random.randint(2, p - 2)
    public_key = pow(g, private_key, p)
    return (public_key, p, g), private_key

def encrypt(plaintext, public_key):
    """
    Encrypt a plaintext message using the ElGamal public key.
    
    Args:
        plaintext (int): The plaintext message as an integer
        public_key (tuple): The ElGamal public key (y, p, g)
        
    Returns:
        tuple: (ciphertext_1, ciphertext_2)
    """
    y, p, g = public_key
    k = random.randint(2, p - 2)
    ciphertext_1 = pow(g, k, p)
    ciphertext_2 = (plaintext * pow(y, k, p)) % p
    return ciphertext_1, ciphertext_2

def decrypt(ciphertext, private_key, p):
    """
    Decrypt a ciphertext using the ElGamal private key.
    
    Args:
        ciphertext (tuple): The ciphertext (ciphertext_1, ciphertext_2)
        private_key (int): The ElGamal private key
        p (int): The prime number used for the key generation
        
    Returns:
        int: The plaintext message as an integer
    """
    ciphertext_1, ciphertext_2 = ciphertext
    plaintext = (ciphertext_2 * pow(ciphertext_1, p - 1 - private_key, p)) % p
    return plaintext

# Example usage
p = 23  # A large prime number
g = find_primitive_root(p)
print(f"Prime number (p): {p}")
print(f"Primitive root (g): {g}")

public_key, private_key = generate_key_pair(p, g)
print(f"Public key: {public_key}")
print(f"Private key: {private_key}")

plaintext = 12
ciphertext = encrypt(plaintext, public_key)
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")

decrypted_text = decrypt(ciphertext, private_key, p)
print(f"Decrypted text: {decrypted_text}")