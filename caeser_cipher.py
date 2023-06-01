alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
             'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def cipher(text, shift_key):
        new_text = ""
        for char in text:
            if char in alphabets:
                position = alphabets.index(char)
                new_position = (position + shift_key) % 26
                new_text += alphabets[new_position]
            else:
                new_text += char
        print(f"The ciphered text is : {new_text}")

wanna_end = False
while not wanna_end:
    what_to_do = input("Type 'encrypt' for encryption, type 'decrypt' for decryption.")
    message = input("Type your message: \n")
    shift = int(input("Enter shift key: \n"))

    if what_to_do == 'encrypt':
        cipher(text = message, shift_key=shift)
    elif what_to_do == 'decrypt':
        shift = shift * (-1)
        cipher(text = message, shift_key=shift)
        
        
    play_again = input("Type'yes' to continue, type 'no' to exit")
    if play_again == 'no':
        wanna_end = True
        print("Have a nice day! Byee...")
        