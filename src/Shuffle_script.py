def railfence(text, rails):
    lines = [''] * rails
    row = 0
    direction = 1 
# 1 = down, -1 = up
    for ch in text:
        lines[row] += ch
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        row += direction
    return ''.join(lines)

file = input("Enter the name of the file: ").strip()
rails = int(input("Enter number of rails (=>2): "))

with open(file, "r", encoding="utf-8") as f:
    text = f.read().strip()

cipher = railfence(text, rails)

with open("shuffle_proprietary.txt", "w", encoding="utf-8") as f:
    f.write(cipher)


