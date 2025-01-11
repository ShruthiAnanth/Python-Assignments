"""
Program takes inputted phrase and encodes it with a rail fence cipher and vigenere cipher,
prints the encoded texts, and then prints the decoded text.
"""

#  Input: string is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of string
#  Output: function returns a single string that is encoded with
#          rail fence algorithm
def rail_fence_encode(string, key):
    """
    Encodes and decodes the given string with a rail fence cipher.

    :string: The string to be encoded.
    :key: The amount of horizontal rails used to encode the text.
    """
    rails = [''] * key
    index = 0
    direction = 1
    for char in string:
        rails[index] += char
        index += direction
        if index in (key, -1):
            direction *= -1
            index += 2 * direction
    return ''.join(rails)


#  Input: string is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of string
#  Output: function returns a single string that is decoded with rail fence algorithm
def rail_fence_decode(string, key):
    """
    Decodes texts encoded with the rail cipher method.

    :string: The text to be encoded.
    :key: The number of horizontal rails used in the decoding process.
    """
    rails = [''] * key
    index = 0
    direction = 1
    for char in string:
        rails[index] += char
        index += direction
        if index in (key, -1):
            direction *= -1
            index += 2 * direction
    decoded_text = ''.join(rails)
    return decoded_text

    #for row in rails:
    #    for col in rails[row]:

#  Input: string is a string of characters
#  Output: function converts all characters to lower case and then
#          removes all digits, punctuation marks, and spaces. It
#          returns a single string with only lower case characters
def filter_string(string):
    """
    Removes all punctuation, digits, spaces, and makes string lowercase.

    :string: The string to be modified:
    """
    return ''.join([char.lower() for char in string if char.isalpha()])


#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character encoded using the
#          Vigenere algorithm. You may not use a 2-D list
def encode_character(p, s):
    """
    Function returns single character using encode algorithm.

    :p: Character in pass phrase.
    :s: Character in plain text.
    """
    return chr((ord(s) + ord(p) - 2 * ord('a')) % 26 + ord('a'))


#  Input: p is a character in the pass phrase and s is a character
#         in the cipher text
#  Output: function returns a single character decoded using the
#          Vigenere algorithm. You may not use a 2-D list
def decode_character(p, s):
    """
    Function returns single character using decode algorithm.

    :p: Character in pass phrase.
    :s: Character in plain text.
    """
    return chr((ord(s) - ord(p) + 26) % 26 + ord('a'))


#  Input: string is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is encoded with
#          Vigenere algorithm
def vigenere_encode(string, phrase):
    """
    Encodes the given string with a vignere cipher.

    :string: The string to be encoded.
    :phrase: The phrase used to encode the text.
    """
    len_str = len(string)
    pass_key = str()
    new_word = str()
    for i in range(len_str):
        pass_key += phrase[i % len(phrase)]

    counter = 0
    for i in string:

        row = ord(i) - 97
        col = ord(pass_key[counter]) - 97
        new_char = ((row + col) % 26) + 97
        new_word += chr(new_char)

        counter += 1

    return new_word  # placeholder for the actual return statement


#  Input: string is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is decoded with
#          Vigenere algorithm
def vigenere_decode(string, phrase):
    """
    Decodes the given string with a vignere cipher.

    :string: The string to be decoded.
    :phrase: The phrase used to decode the text.
    """
    len_str = len(string)
    pass_key = str()
    new_word = str()
    for i in range(len_str):
        pass_key += phrase[i % len(phrase)]

    counter = 0
    for i in string:

        row = ord(i) - 97
        col = ord(pass_key[counter]) - 97
        new_char = ((row - col) % 26) + 97
        new_word += chr(new_char)

        counter += 1

    return new_word 


def main():
    """
    Runs encode and decode functions, prints outputted text.
    """
    # read the plain text from stdin
    plain_text_rail = input().strip()
    # read the key from stdin
    key_rail = int(input().strip())
    # encode and print the encoded text using rail fence cipher
    print("Rail Fence Cipher")
    print(f"Plain Text: {plain_text_rail}")
    print(f"Key: {key_rail}")
    encoded_text_rail = rail_fence_encode(plain_text_rail, key_rail)
    print(f"Encoded Text: {encoded_text_rail}")
    # read encoded text from stdin
    cipher_text_rail = input().strip()
    # read the key from stdin
    key_rail_decode = int(input().strip())
    # decode and print the plain text using rail fence cipher
    print("Enter Key:", key_rail_decode)
    decoded_text_rail = rail_fence_decode(cipher_text_rail, key_rail_decode)
    print(f"Decoded Text: {decoded_text_rail}")
    # read the plain text from stdin
    plain_text_vigenere = input().strip()
    # read the pass phrase from stdin
    passphrase_vigenere = input().strip()
    # encode and print the encoded text using Vigenere cipher
    print("\nVigenere Cipher")
    print(f"Plain Text: {plain_text_vigenere}")
    print(f"Pass Phrase: {passphrase_vigenere}")
    encoded_text_vigenere = vigenere_encode(plain_text_vigenere, passphrase_vigenere)
    print(f"Encoded Text: {encoded_text_vigenere}")
    # read the encoded text from stdin
    encoded_text_vigenere_decode = input().strip()
    # read the pass phrase from stdin
    passphrase_vigenere_decode = input().strip()
    # decode and print the plain text using Vigenere cipher
    print(f"Pass Phrase: {passphrase_vigenere_decode}")
    decoded_text_vigenere = vigenere_decode(encoded_text_vigenere_decode,
                                             passphrase_vigenere_decode)
    print(f"Decoded Text: {decoded_text_vigenere}")
# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()
    
