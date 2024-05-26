def rail_fence_encrypt(message, num_rails):
    if num_rails == 1:
        return message

    
    matrix = [[''] * len(message) for _ in range(num_rails)]

    row, direction = 0, 1
    for i, char in enumerate(message):
        matrix[row][i] = char
        row += direction
        if row == num_rails or row == -1:
            direction *= -1
            row += 2 * direction

   
    encrypted_message = ''.join(''.join(row) for row in matrix)
    return encrypted_message

def rail_fence_decrypt(encrypted_message, num_rails):
    if num_rails == 1:
        return encrypted_message

   
    matrix = [[''] * len(encrypted_message) for _ in range(num_rails)]

    row, direction = 0, 1
    for i in range(len(encrypted_message)):
        matrix[row][i] = '*'
        row += direction
        if row == num_rails or row == -1:
            direction *= -1
            row += 2 * direction

   
    idx = 0
    for r in range(num_rails):
        for c in range(len(encrypted_message)):
            if matrix[r][c] == '*':
                matrix[r][c] = encrypted_message[idx]
                idx += 1

   
    decrypted_message = ''
    row, direction = 0, 1
    for i in range(len(encrypted_message)):
        if matrix[row][i] != ' ':
            decrypted_message += matrix[row][i]
        row += direction
        if row == num_rails or row == -1:
            direction *= -1
            row += 2 * direction

    return decrypted_message


if __name__ == "__main__":
    full_name = "KushalAcharya"  
    num_rails = 3  

    encrypted_name = rail_fence_encrypt(full_name.replace(" ", ""), num_rails)
    decrypted_name = rail_fence_decrypt(encrypted_name, num_rails)

    print(f"Original Name: {full_name}")
    print(f"Encrypted Name: {encrypted_name}")
    print(f"Decrypted Name: {decrypted_name}")
