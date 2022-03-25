def solution(x):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decoded_message = ""

    for letter in x:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            decoded_message += alphabet[-letter_index-1]
        else:
            decoded_message += letter
    return decoded_message
