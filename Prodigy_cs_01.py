def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(text, shift):
    return encrypt(text, -shift)


def main():
    while True:
        choice = input("Enter 'e' for encrypting and 'd' decrypting a message? : ").lower()
        if choice in ['e', 'd']:
            text = input("Enter the message: ")
            shift = int(input("Enter the shift value(Key): "))

            if choice == 'e':
                encrypted_message = encrypt(text, shift)
                print(f"Encrypted Message: {encrypted_message}")
            elif choice == 'd':
                decrypted_message = decrypt(text, shift)
                print(f"Decrypted Message: {decrypted_message}")
        else:
            print("Invalid choice. Please choose 'e' to encrypt or 'd' to decrypt.")

        cont = input("Do you want to encrypt/decrypt another message? (yes/no): ").lower()
        if cont != 'yes':
            break

if __name__ == "__main__":
    main()
