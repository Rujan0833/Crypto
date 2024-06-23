def phi(n):
    """
    Compute Euler's Totient Function, which counts the number of positive integers less than or equal to n that are relatively prime to n.
    """
    result = n
    for i in range(2, n + 1):
        if gcd(i, n) == 1:
            result -= 1
    return result

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
    phi_n = phi(n)
    roots = set()
    for r in range(1, phi_n):
        roots.add(pow(g, r, n))
    return len(roots) == phi_n - 1

def find_primitive_roots(n):
    """
    Find the primitive roots of a prime number n.
    """
    primitive_roots = []
    for g in range(2, n):
        if gcd(g, n) == 1 and is_primitive_root(g, n):
            primitive_roots.append(g)
    return primitive_roots

# Example usage
p = 17
roots = find_primitive_roots(p)
print(f"The primitive roots of {p} are: {roots}")