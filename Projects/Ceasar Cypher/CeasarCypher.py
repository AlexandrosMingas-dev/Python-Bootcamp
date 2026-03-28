import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text,shift):
    text_encrypted = ""
    for letter in text:
        for i in range(len(alphabet)):
            if letter == alphabet[i]:
                 text_encrypted+= alphabet[(i+shift)%26]
            elif letter not in alphabet:
                text_encrypted+= letter
                break
    return text_encrypted

def decrypt(text,shift):
    text_decrypted = ""
    for letter in text:
        for i in range(len(alphabet)):
            if letter == alphabet[i]:
                 text_decrypted+= alphabet[(i-shift)%26]
            elif letter not in alphabet:
                text_decrypted+= letter
                break
    return text_decrypted

#MAIN
logo= art.logo
print(logo)
cont='Y'
flag=False
while cont=='Y' or cont=='y':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction.lower() == 'encode':
        encrypted_text=encrypt(text,shift)
        print("The encrypted message is:",encrypted_text)
        cont=input("Do you want to continue ? (Y/N) ")
    else:
        decrypted_text=decrypt(text,shift)
        print("The encrypted message is:", decrypted_text)
        cont=input("Do you want to continue ? (Y/N) ")

