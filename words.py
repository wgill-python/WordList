def num_letters(num_rows, num_columns):
    return 2 * num_rows + 2 * num_columns - 4
assert num_letters(13,4)==30
assert num_letters(4,4)==12
assert num_letters(4,6)==16
assert num_letters(7,6)==22
print("Checking assertions.")

