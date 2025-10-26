def railfence_decrypt(cipher, rails):
    n = len(cipher)
    grid = [['' for _ in range(n)] for _ in range(rails)]

    row = 0
    direction = 1
    for i in range(n):
        grid[row][i] = '*'
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        row += direction

    index = 0
    for r in range(rails):
        for c in range(n):
            if grid[r][c] == '*':
                grid[r][c] = cipher[index]
                index += 1

    result = []
    row = 0
    direction = 1
    for i in range(n):
        result.append(grid[row][i])
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        row += direction
    return ''.join(result)

with open("shuffle_proprietary.txt", "r", encoding="utf-8") as f:
    cipher = f.read().strip()

with open("passwd.txt", "r") as f:
    rails = int(f.read().strip())

decrypted = railfence_decrypt(cipher, rails)

with open("plain_out.txt", "w", encoding="utf-8") as f:
    f.write(decrypted)
