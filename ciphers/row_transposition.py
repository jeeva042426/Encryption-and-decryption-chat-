def encrypt(text, key):
    key = [int(k) for k in key]
    col_count = len(key)
    rows = [text[i:i + col_count] for i in range(0, len(text), col_count)]

    for i in range(len(rows)):
        if len(rows[i]) < col_count:
            rows[i] += 'X' * (col_count - len(rows[i]))

    sorted_key = sorted((num, i) for i, num in enumerate(key))
    encrypted = ''
    for num, i in sorted_key:
        encrypted += ''.join(row[i] for row in rows)

    return encrypted

def decrypt(cipher, key):
    key = [int(k) for k in key]
    col_count = len(key)
    row_count = len(cipher) // col_count
    sorted_key = sorted((num, i) for i, num in enumerate(key))

    # Create empty matrix
    matrix = [[''] * col_count for _ in range(row_count)]

    # Fill columns according to sorted key
    k = 0
    for num, original_pos in sorted_key:
        for r in range(row_count):
            matrix[r][original_pos] = cipher[k]
            k += 1

    # Flatten
    return ''.join(''.join(row) for row in matrix).rstrip('X')
