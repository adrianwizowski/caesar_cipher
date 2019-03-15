import string
from typing import Dict

from dict_loader import loader


def decrypt(plaintext: str, n: int) -> str:
    """
    Decrypt Caesar Cipher using decrypting shift.

    :param plaintext: text to decrypt
    :type plaintext: str
    :param n: decrypting shift
    :type n: int
    :return: decrypted text
    :rtype: str
    """
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[-n:] + alphabet[:-n]
    plaintext = plaintext.lower()
    table = plaintext.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)


def encrypt(plaintext: str, n: int) -> str:
    """
    Encrypt Caesar Cipher using encrypting shift.

    :param plaintext: text to encrypt
    :type plaintext: str
    :param n: encrypting shift
    :type n: int
    :return: encrypted text
    :rtype: str
    """
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[n:] + alphabet[:n]
    plaintext = plaintext.lower()
    table = plaintext.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)


def break_the_code(plaintext: str, words: Dict) -> str:
    """
    Breaks Caesar Cipher. Returns most possible decrypted result.

    :param plaintext: text to break
    :type plaintext: str
    :param words: dict with words used to break the code
    :type words: dict
    :return: most possible encrypted text
    :rtype: str
    """
    all_results = {}
    for n in range(len(string.ascii_lowercase)):
        match_counter = 0
        plaintext = plaintext.lower()
        decrypted = decrypt(plaintext, n)
        for word in decrypted.split(" "):
            try:
                if words[word.rstrip(' ,./?!@#$%^&*(){}[]')]:
                    match_counter += 1
            except KeyError:
                pass
        all_results[decrypted] = round(
            match_counter / len(decrypted.split(" ")) * 100, 2
        )
    match = sorted(all_results.items(), key=lambda x: x[1], reverse=True)[0]
    if match[1] == 0.0:
        return f"Unable to break: {match[0]}"
    return f"Most possible match: {match[0]} - possibility = {match[1]}%"


def quit_cipher():
    """Ends up Caesar Cipher program by raising SystemExit."""
    print("Bye Bye.")
    raise SystemExit


def run_cipher(words):
    """Main Caesar Cipher function with simple menu."""
    menu = {"e": encrypt, "d": decrypt, "b": break_the_code}

    running = True
    while running:
        choice = input(
            "What would you like to do? Encrypt (e), decrypt (b), break (b) or quit (q)? "
        )
        if choice == "q":
            quit_cipher()
        try:
            plaintext = input("Please provide text to encrypt/decrypt/break: ")
            shift = input("Please provide code shift number if necessary: ")
            if choice == "b":
                if input_validator(plaintext, shift, break_it=True):
                    print(menu[choice](plaintext, words))
            else:
                if input_validator(plaintext, shift):
                    print(menu[choice](plaintext, int(shift)))
        except KeyError:
            print("Invalid menu option.")
            pass


def input_validator(plaintext: str, shift: str, break_it: bool = False) -> bool:
    """
    Validate user input. Returns True if valid.

    :param plaintext: text provided by user
    :type plaintext: str
    :param shift: shift provided by user
    :type shift: str
    :param break_it: Determines if shift should be validated or not
    :type break_it: boolean
    :return: boolean
    """
    if not plaintext or not shift and not break_it:
        print("Invalid text or shift.")
        return False
    if not break_it:
        try:
            int(shift)
        except ValueError:
            print("Shift should be an integer.")
            return False
    elif break_it and not plaintext:
        print("Invalid text.")
        return False
    return True


if __name__ == "__main__":
    run_cipher(loader())
