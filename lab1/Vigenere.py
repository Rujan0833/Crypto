def generate_key(message, key):
    key = list(key)
    if len(message) == len(key):
        return key
    else:
        key = list(key)
        new_key = []
        key_index = 0
        for char in message:
            if char.isalpha():
                new_key.append(key[key_index % len(key)])
                key_index += 1
            else:
                new_key.append(char)
        return ''.join(new_key)

def vigenere_encrypt(message, key):
    encrypted_text = []
    for i in range(len(message)):
        if message[i].isalpha():
            shift = ord(key[i]) - ord('A')
            if message[i].isupper():
                encrypted_text.append(chr((ord(message[i]) + shift - 65) % 26 + 65))
            else:
                encrypted_text.append(chr((ord(message[i]) + shift - 97) % 26 + 97))
        else:
            encrypted_text.append(message[i])
    return ''.join(encrypted_text)

def vigenere_decrypt(encrypted_message, key):
    decrypted_text = []
    for i in range(len(encrypted_message)):
        if encrypted_message[i].isalpha():
            shift = ord(key[i]) - ord('A')
            if encrypted_message[i].isupper():
                decrypted_text.append(chr((ord(encrypted_message[i]) - shift - 65) % 26 + 65))
            else:
                decrypted_text.append(chr((ord(encrypted_message[i]) - shift - 97) % 26 + 97))
        else:
            decrypted_text.append(encrypted_message[i])
    return ''.join(decrypted_text)

if __name__ == "__main__":
    full_name = "Kushal"  
    keyword = "MOUNTAIN"  
    
   
    key = generate_key(full_name.upper(), keyword.upper())
    
    encrypted_name = vigenere_encrypt(full_name, key)
    decrypted_name = vigenere_decrypt(encrypted_name, key)
    
    print(f"Original Name: {full_name}")
    print(f"Encrypted Name: {encrypted_name}")
    print(f"Decrypted Name: {decrypted_name}")
