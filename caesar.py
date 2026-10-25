while True:
    letter = input("Enter a letter (or 'exit' to quit): ")
    if letter.lower() == 'exit':
        exit()
    if len(letter) != 1:
        print("Please enter a single letter.")
        continue
    if not letter.isalpha():
        print("Please enter a letter.")
        continue
    letter = letter.lower()
    break

max_shift = ord('z') - ord(letter)

while True:
    text = input(f"Enter a number between 1 and {max_shift}: ")

    try:
        shift = int(text)
    except ValueError:
        print("Please enter a valid number.")
        continue

    if 1 <= shift <= max_shift:
        break
    else:
        print(f"Please enter a number between 1 and {max_shift}.")

new_letter = chr(ord(letter) + shift)
print(letter, "->", new_letter)