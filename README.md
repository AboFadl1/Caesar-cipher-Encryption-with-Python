# Caesar Cipher Text Encryptor & Decryptor 🔐

A simple Python project that implements a **Caesar Cipher** to encrypt and decrypt text files.  
The program reads a `.txt` file, shifts each letter by a user-specified key, and saves the result into a new file.

---

## 📌 Features
- Encrypts plain text files using Caesar cipher.
- Decrypts encrypted files back into readable text (using the same key).
- Works with both **uppercase** and **lowercase** letters.
- Leaves numbers, punctuation, and spaces unchanged.
- Saves results as new files (`encryption.txt` / `decryption.txt`).
- Simple interactive **menu** for choosing encryption or decryption.

---

## 🚀 How It Works
1. **Encryption**
   - Reads a text file.
   - Shifts each alphabetical character by the given key (e.g., `a → d` with key = 3).
   - Saves the result into `encryption.txt`.

2. **Decryption**
   - Reads an encrypted text file.
   - Reverses the shift using the same key.
   - Saves the result into `decryption.txt`.

---

## 🛠️ Requirements
- Python **3.6+**
- No external libraries required (uses only built-in Python functions).

## ▶️ Usage
1. Clone the repository:
