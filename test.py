table = [
    ("ABCDEFGHIJKLM", "NOPQRSTUVWXYZ"),
    ("ABCDEFGHIJKLM", "YZNOPQRSTUVWX"),
    ("ABCDEFGHIJKLM", "RSTUVWXYZNOPQ"),
    ("ABCDEFGHIJKLM", "VWXYZNOPQRSTU"),
    ("ABCDEFGHIJKLM", "TUVWXYZNOPQRS"),
    ("ABCDEFGHIJKLM", "XYZNOPQRSTUVW"),
    ("ABCDEFGHIJKLM", "VWXYZNOPQRSTU"),
    ("ABCDEFGHIJKLM", "YZNOPQRSTUVWX"),
    ("ABCDEFGHIJKLM", "OPQRSTUVWXYZN"),
]


def get_position(table, char):
    if char in table[0]:
        row = 0
    else:
        row = 1 if char in table[1] else -1
    print(f"char: {row}")
    return (None, None) if row == -1 else (row, table[row].index(char))


def get_opponent(table, char):
    row, col = get_position(table, char.upper())
    print(f"get position: {row, col}")
    if row == 1:
        return table[0][col]
    else:
        return table[1][col] if row == 0 else char


def encrypt(words):
    cipher = ""
    count = 0

    for char in words.upper():
        cipher += get_opponent(table[count], char)
        count = (count + 1) % len(table)
        print(f"Cipher: {cipher}")
    return cipher


encrypt("defend the east berlin")
