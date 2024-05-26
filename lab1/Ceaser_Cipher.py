def encryption(text, shift_len):
    result = ""
    for i in range(len(text)):
        char = text[i]
        #capital letter
        if char.isupper():
            result += chr((ord(char) + shift_len - 65) % 26 + 65)
        #small letter
        elif char.islower():
            result += chr((ord(char) + shift_len- 97) % 26 + 97)
        else:
            result += char
    return result

def decryption(text, shift_len):
    result = ""
    for i in range(len(text)):
        char = text[i]
        # Decrypt Capital letter
        if char.isupper():
            result += chr((ord(char) - shift_len - 65) % 26 + 65)
        # Decrypt small letter
        elif char.islower():
            result += chr((ord(char) - shift_len - 97) % 26 + 97)
        else:
            result += char
    return result

if __name__ == "__main__":
    full_name = "Kushal Acharya"  
    shift_len= 7  
    
    encrypted = encryption(full_name, shift_len)
    decrypted = decryption(encrypted, shift_len)
    
    print(f"Original Name: {full_name}")
    print(f"Encrypted Name: {encrypted}")
    print(f"Decrypted Name: {decrypted}")
