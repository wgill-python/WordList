def num_letters(num_rows, num_columns):
    return 2 * num_rows + 2 * num_columns - 4
assert num_letters(13,4)==30
assert num_letters(4,4)==12
assert num_letters(4,6)==16
assert num_letters(7,6)==22
print("Checking assertions.")

import numpy as np
data = np.loadtxt("loop1.csv", delimiter=",", dtype=str, encoding="utf8")
words = []

rows, columns = data.shape

for col in range(columns):
    words.append(data[0, col])

for row in range(1, rows):
    words.append(data[row, columns - 1])

for col in range(columns - 2, -1, -1):
    words.append(data[rows - 1,col])

for row in range(rows - 2, 0, -1):
    words.append(data[row, 0])
print(words)

assert len(words) == num_letters(rows, columns)


import numpy as np
data = np.loadtxt("loop1.csv", delimiter=",", dtype=str, encoding="utf8")
letters = []

rows, columns = data.shape

for col in range(columns):
    letters.append(data[0, col])

for row in range(1, rows):
    letters.append(data[row, columns - 1])

for col in range(columns - 2, -1, -1):
    letters.append(data[rows - 1,col])

for row in range(rows - 2, 0, -1):
    letters.append(data[row, 0])
words = []
for i in range(len(letters)):
    next_index = (i + 1) % len(letters)
    words.append(letters[i] + letters[next_index])
    


print(words)

assert len(words) == num_letters(rows, columns)


