def generate_playfair_key_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = key.upper().replace('J', 'I')
    key_matrix = []
    used_chars = set()

    for char in key:
        if char not in used_chars and char in alphabet:
            key_matrix.append(char)
            used_chars.add(char)

    for char in alphabet:
        if char not in used_chars:
            key_matrix.append(char)
            used_chars.add(char)

    return [key_matrix[i * 5:(i + 1) * 5] for i in range(5)]

def preprocess_message(message):
    message = message.upper().replace('J', 'I').replace(' ', '')
    processed_message = []

    i = 0
    while i < len(message):
        a = message[i]
        if i + 1 < len(message):
            b = message[i + 1]
            if a != b:
                processed_message.append(a + b)
                i += 2
            else:
                processed_message.append(a + 'X')
                i += 1
        else:
            processed_message.append(a + 'X')
            i += 1

    return processed_message

def find_position(char, key_matrix):
    for i, row in enumerate(key_matrix):
        for j, matrix_char in enumerate(row):
            if char == matrix_char:
                return i, j
    return None

def playfair_encrypt(message, key_matrix):
    digraphs = preprocess_message(message)
    encrypted_message = []

    for digraph in digraphs:
        a, b = digraph[0], digraph[1]
        row_a, col_a = find_position(a, key_matrix)
        row_b, col_b = find_position(b, key_matrix)

        if row_a == row_b:
            encrypted_message.append(key_matrix[row_a][(col_a + 1) % 5])
            encrypted_message.append(key_matrix[row_b][(col_b + 1) % 5])
        elif col_a == col_b:
            encrypted_message.append(key_matrix[(row_a + 1) % 5][col_a])
            encrypted_message.append(key_matrix[(row_b + 1) % 5][col_b])
        else:
            encrypted_message.append(key_matrix[row_a][col_b])
            encrypted_message.append(key_matrix[row_b][col_a])

    return ''.join(encrypted_message)

def playfair_decrypt(encrypted_message, key_matrix):
    digraphs = preprocess_message(encrypted_message)
    decrypted_message = []

    for digraph in digraphs:
        a, b = digraph[0], digraph[1]
        row_a, col_a = find_position(a, key_matrix)
        row_b, col_b = find_position(b, key_matrix)

        if row_a == row_b:
            decrypted_message.append(key_matrix[row_a][(col_a - 1) % 5])
            decrypted_message.append(key_matrix[row_b][(col_b - 1) % 5])
        elif col_a == col_b:
            decrypted_message.append(key_matrix[(row_a - 1) % 5][col_a])
            decrypted_message.append(key_matrix[(row_b - 1) % 5][col_b])
        else:
            decrypted_message.append(key_matrix[row_a][col_b])
            decrypted_message.append(key_matrix[row_b][col_a])

    return ''.join(decrypted_message)

if __name__ == "__main__":
    full_name = "Kushal Acharya"  
    key = "PANDALOL"  

    key_matrix = generate_playfair_key_matrix(key)
    encrypted_name = playfair_encrypt(full_name, key_matrix)
    decrypted_name = playfair_decrypt(encrypted_name, key_matrix)

    print(f"Original Name: {full_name}")
    print(f"Encrypted Name: {encrypted_name}")
    print(f"Decrypted Name: {decrypted_name}")
