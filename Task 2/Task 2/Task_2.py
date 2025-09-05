def encrypt():
    input_file = input("Enter Text File Path: ")
    input_file = input_file.replace('\\', "/")
    input_file = input_file.replace('"', "")
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    import os
    folder = os.path.dirname(input_file)
    file_name = os.path.join(folder, "encryption.txt")
    key = int(input("Enter key number: "))

    encrypted_words = []

    words = content.split()
    for word in words:
        encrypted_word = ""
        for letter in word:
            if letter.isalpha():
              base = 65 if letter.isupper() else 97
              encrypted_word += chr((ord(letter) - base + key) % 26 + base)
            else:
              encrypted_word += letter
        encrypted_words.append(encrypted_word)

    new_content = ' '.join(encrypted_words)
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"✅ Encryption complete! Saved to {file_name}")

def decrypt():
    input_file = input("Enter Encrypted File Path: ")
    input_file = input_file.replace('\\', "/")
    input_file = input_file.replace('"', "")
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    import os
    folder = os.path.dirname(input_file)
    file_name = os.path.join(folder, "decryption.txt")
    key = int(input("Enter key number: "))

    decrypted_words = []

    words = content.split()
    for word in words:
        decrypted_word = ""
        for letter in word:
            if letter.isalpha():
              base = 65 if letter.isupper() else 97
              decrypted_word += chr((ord(letter) - base - key) % 26 + base)
            else:
              decrypted_word += letter
        decrypted_words.append(decrypted_word)

    new_content = ' '.join(decrypted_words)
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"✅ Decryption complete! Saved to {file_name}")

menu = """
1. Encrypt
2. Decrypt
"""
print(menu)
choice = input("Enter Choice number: ")
if choice == "1":
   encrypt()
elif choice == "2":
   decrypt()
else:
    print("Invalid input, please enter number between 1 and 2")
