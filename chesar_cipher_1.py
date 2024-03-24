alphabet = 'abcdefghijklmnopqrstuvwxyz'

direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt: ")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)  # index is a build-in python function that returns the index of the first
            # encountered character
            new_position = (position + shift_amount) % 26
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += letter
    print(f"The encrypted text is: {cipher_text}")


def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position - shift_amount) % 26
            new_letter = alphabet[new_position]
            plain_text += new_letter
        else:
            plain_text += letter
    print(f"The decoded text is: {plain_text}")


if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("Wrong selection!! run again..")
