import numpy as np


def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1

#
def matrix_mod_inverse(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix))) 
    det_inv = mod_inverse(det, modulus)  
    if det_inv == -1:
        raise ValueError("Matrix is not invertible")
    
    matrix_modulus_inv = (
        det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    )
    return matrix_modulus_inv % modulus


def hill_encrypt(message, key):
    message = message.replace(" ", "").upper()
    length = len(key)
    if len(message) % length != 0:
        message += "X" * (length - len(message) % length)  
    
    message_vector = [ord(char) - 65 for char in message]
    encrypted_vector = []
    
    for i in range(0, len(message_vector), length):
        chunk = message_vector[i:i+length]
        encrypted_chunk = np.dot(key, chunk) % 26
        encrypted_vector.extend(encrypted_chunk)
    
    encrypted_text = ''.join(chr(num + 65) for num in encrypted_vector)
    return encrypted_text

# Function to decrypt 
def hill_decrypt(encrypted_message, key):
    length = len(key)
    encrypted_vector = [ord(char) - 65 for char in encrypted_message]
    decrypted_vector = []
    
    key_inv = matrix_mod_inverse(key, 26)
    
    for i in range(0, len(encrypted_vector), length):
        chunk = encrypted_vector[i:i+length]
        decrypted_chunk = np.dot(key_inv, chunk) % 26
        decrypted_vector.extend(decrypted_chunk)
    
    decrypted_text = ''.join(chr(int(num) + 65) for num in decrypted_vector)
    return decrypted_text

if __name__ == "__main__":
    full_name = "Kushal Acharya"  # Replace with your full name
    key = np.array([[7, 22, 10], [23, 12, 1], [2, 17, 15]])  # 3x3 Key matrix

    encrypted_name = hill_encrypt(full_name, key)
    decrypted_name = hill_decrypt(encrypted_name, key)
    
    print(f"Original Name: {full_name}")
    print(f"Encrypted Name: {encrypted_name}")
    print(f"Decrypted Name: {decrypted_name}")
