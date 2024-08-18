# add your code here

def encrypt(text, shift):
    text = text.lower ()
    encrypted_text = ""
    for char in text:
        if char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

originalSentence = "python is fun!"
encryptedSentence = encrypt(originalSentence, 5)
print(encryptedSentence)