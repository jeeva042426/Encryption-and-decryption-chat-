def encrypt(text, key):
    if key <= 1:
        return text
    rails = ['' for _ in range(key)]
    direction_down = False
    row = 0

    for char in text.replace(" ", ""):
        rails[row] += char
        if row == 0 or row == key - 1:
            direction_down = not direction_down
        row += 1 if direction_down else -1

    return ''.join(rails)

def decrypt(cipher, key):
    if key <= 1:
        return cipher

    pattern = [[] for _ in range(key)]
    direction_down = False
    row = 0

    # Step 1: Mark the zigzag positions
    for i in range(len(cipher)):
        pattern[row].append(i)
        if row == 0 or row == key - 1:
            direction_down = not direction_down
        row += 1 if direction_down else -1

    # Step 2: Flatten the pattern and fill characters
    index_positions = [i for row in pattern for i in row]
    plain = [''] * len(cipher)
    for idx, char in zip(index_positions, cipher):
        plain[idx] = char

    return ''.join(plain)
