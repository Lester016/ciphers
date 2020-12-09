alphabet = {
    "A": ("ABCDEFGHIJKLM", "NOPQRSTUVWXYZ"),
    "B": ("ABCDEFGHIJKLM", "NOPQRSTUVWXYZ"),
    "C": ("ABCDEFGHIJKLM", "ZNOPQRSTUVWXY"),
    "D": ("ABCDEFGHIJKLM", "ZNOPQRSTUVWXY"),
    "E": ("ABCDEFGHIJKLM", "YZNOPQRSTUVWX"),
    "F": ("ABCDEFGHIJKLM", "YZNOPQRSTUVWX"),
    "G": ("ABCDEFGHIJKLM", "XYZNOPQRSTUVW"),
    "H": ("ABCDEFGHIJKLM", "XYZNOPQRSTUVW"),
    "I": ("ABCDEFGHIJKLM", "WXYZNOPQRSTUV"),
    "J": ("ABCDEFGHIJKLM", "WXYZNOPQRSTUV"),
    "K": ("ABCDEFGHIJKLM", "VWXYZNOPQRSTU"),
    "L": ("ABCDEFGHIJKLM", "VWXYZNOPQRSTU"),
    "M": ("ABCDEFGHIJKLM", "UVWXYZNOPQRST"),
    "N": ("ABCDEFGHIJKLM", "UVWXYZNOPQRST"),
    "O": ("ABCDEFGHIJKLM", "TUVWXYZNOPQRS"),
    "P": ("ABCDEFGHIJKLM", "TUVWXYZNOPQRS"),
    "Q": ("ABCDEFGHIJKLM", "STUVWXYZNOPQR"),
    "R": ("ABCDEFGHIJKLM", "STUVWXYZNOPQR"),
    "S": ("ABCDEFGHIJKLM", "RSTUVWXYZNOPQ"),
    "T": ("ABCDEFGHIJKLM", "RSTUVWXYZNOPQ"),
    "U": ("ABCDEFGHIJKLM", "QRSTUVWXYZNOP"),
    "V": ("ABCDEFGHIJKLM", "QRSTUVWXYZNOP"),
    "W": ("ABCDEFGHIJKLM", "PQRSTUVWXYZNO"),
    "X": ("ABCDEFGHIJKLM", "PQRSTUVWXYZNO"),
    "Y": ("ABCDEFGHIJKLM", "OPQRSTUVWXYZN"),
    "Z": ("ABCDEFGHIJKLM", "OPQRSTUVWXYZN"),
}


def generate_table(key):
    """
    >>> generate_table('betlogkey')  # doctest: +NORMALIZE_WHITESPACE
    [('ABCDEFGHIJKLM', 'NOPQRSTUVWXYZ'),
    ('ABCDEFGHIJKLM', 'YZNOPQRSTUVWX'),
    ('ABCDEFGHIJKLM', 'RSTUVWXYZNOPQ'),
    ('ABCDEFGHIJKLM', 'VWXYZNOPQRSTU'),
    ('ABCDEFGHIJKLM', 'TUVWXYZNOPQRS'),
    ('ABCDEFGHIJKLM', 'XYZNOPQRSTUVW'),
    ('ABCDEFGHIJKLM', 'VWXYZNOPQRSTU'),
    ('ABCDEFGHIJKLM', 'YZNOPQRSTUVWX'),
    ('ABCDEFGHIJKLM', 'OPQRSTUVWXYZN')]
    """
    return [alphabet[char] for char in key.upper()]


def encrypt(key, words):
    """
    >>> encrypt('betlogkey', 'defend the east berlin')
    'QPWZHN IVR VVMJ ZSEWZF'
    """
    cipher = ""
    count = 0
    table = generate_table(key)
    for char in words.upper():
        cipher += get_opponent(table[count], char)
        count = (count + 1) % len(table)
    return cipher


def decrypt(key, words):
    """
    >>> decrypt('betlogkey', 'QPWZHN IVR VVMJ ZSEWZF')
    'DEFEND THE EAST BERLIN'
    """
    return encrypt(key, words)


def get_position(table, char):
    """
    >>> table = [
    ... ('ABCDEFGHIJKLM', 'NOPQRSTUVWXYZ'),
    ... ('ABCDEFGHIJKLM', 'YZNOPQRSTUVWX'),
    ... ('ABCDEFGHIJKLM', 'RSTUVWXYZNOPQ'),
    ... ('ABCDEFGHIJKLM', 'VWXYZNOPQRSTU'),
    ... ('ABCDEFGHIJKLM', 'TUVWXYZNOPQRS'),
    ... ('ABCDEFGHIJKLM', 'XYZNOPQRSTUVW'),
    ... ('ABCDEFGHIJKLM', 'VWXYZNOPQRSTU'),
    ... ('ABCDEFGHIJKLM', 'YZNOPQRSTUVWX'),
    ... ('ABCDEFGHIJKLM', 'OPQRSTUVWXYZN')]
    >>> get_position(table, 'A')
    (None, None)
    """
    if char in table[0]:
        row = 0
    else:
        row = 1 if char in table[1] else -1
    return (None, None) if row == -1 else (row, table[row].index(char))


def get_opponent(table, char):
    """
    >>> table = [
    ... ('ABCDEFGHIJKLM', 'NOPQRSTUVWXYZ'),
    ... ('ABCDEFGHIJKLM', 'YZNOPQRSTUVWX'),
    ... ('ABCDEFGHIJKLM', 'RSTUVWXYZNOPQ'),
    ... ('ABCDEFGHIJKLM', 'VWXYZNOPQRSTU'),
    ... ('ABCDEFGHIJKLM', 'TUVWXYZNOPQRS'),
    ... ('ABCDEFGHIJKLM', 'XYZNOPQRSTUVW'),
    ... ('ABCDEFGHIJKLM', 'VWXYZNOPQRSTU'),
    ... ('ABCDEFGHIJKLM', 'YZNOPQRSTUVWX'),
    ... ('ABCDEFGHIJKLM', 'OPQRSTUVWXYZN')]
    >>> get_opponent(table, 'A')
    'A'
    """
    row, col = get_position(table, char.upper())
    if row == 1:
        return table[0][col]
    else:
        return table[1][col] if row == 0 else char


# This function generates the
# key in a cyclic manner until
# it's length isn't equal to
# the length of original text
def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return key
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)


# This function returns the
# encrypted text generated
# with the help of the key
def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i])) % 26
        x += ord("A")
        cipher_text.append(chr(x))
    return "".join(cipher_text)


# This function decrypts the
# encrypted text and returns
# the original text
def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord("A")
        orig_text.append(chr(x))
    return "".join(orig_text)


# Driver code
if __name__ == "__main__":
    import doctest

    doctest.testmod()  # Fist ensure that all our tests are passing...
    """
    ENTER KEY: betlogkey
    ENTER TEXT TO ENCRYPT: defend the east berlin
    ENCRYPTED: QPWZHN IVR VVMJ ZSEWZF
    DECRYPTED WITH KEY: DEFEND THE EAST BERLIN
    """
    key = input("ENTER KEY: ").strip()
    text = input("ENTER TEXT TO ENCRYPT: ").strip()
    cipher_text = encrypt(key, text)

    # print(f"ENCRYPTED: {cipher_text}")
    # print(f"DECRYPTED WITH KEY: {decrypt(key, cipher_text)}")

    string = text.upper()
    keyword = cipher_text
    key = generateKey(string, keyword)
    cipher_text = cipherText(string, key)
    print("ENCRYPTED:", cipher_text)
    print("DECRYPTED WITH KEY:", originalText(cipher_text, key))
