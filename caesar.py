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