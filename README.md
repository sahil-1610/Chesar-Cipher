# Caesar Cipher

## Introduction
The Caesar Cipher is a simple and widely known encryption technique that uses substitution to shift letters in the alphabet by a fixed number of positions. It is a type of monoalphabetic cipher and one of the earliest known encryption methods.

## Features
- Encrypts plaintext using a shift key
- Decrypts ciphertext back to plaintext
- Supports uppercase and lowercase letters
- Can handle custom shift values

## How It Works
Each letter in the plaintext is shifted forward in the alphabet by a fixed number of positions determined by the shift key. If the shift reaches the end of the alphabet, it wraps around to the beginning.

For example, with a shift key of `3`:
- Plaintext: `HELLO`
- Ciphertext: `KHOOR`

## Installation
To use this implementation, clone the repository and navigate to the project directory:

Fork this Repo : 
```sh
git clone https://github.com/AdityaPatadiya/Chesar-Cipher.git
cd caesar-cipher
```

## Usage
### Encryption
```python
from caesar_cipher import encrypt

plaintext = "HELLO"
shift = 3
ciphertext = encrypt(plaintext, shift)
print("Encrypted Text:", ciphertext)
```

### Decryption
```python
from caesar_cipher import decrypt

ciphertext = "KHOOR"
shift = 3
plaintext = decrypt(ciphertext, shift)
print("Decrypted Text:", plaintext)
```

## Example
```sh
Input: HELLO, Shift: 3
Output: KHOOR
```

## Limitations
- Only supports alphabetic characters (A-Z, a-z)
- Does not encrypt numbers or special characters

## License
This project is open-source and available under the MIT License.

