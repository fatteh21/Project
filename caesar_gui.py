import tkinter as tk


def shift_letter():
    letter = letter_entry.get()
    text = number_entry.get()

    # ---------- Check the letter ----------
    if len(letter) != 1:
        result_label.config(text="Please enter a single letter.")
        return
    if not letter.isalpha():
        result_label.config(text="Please enter a letter.")
        return
    letter = letter.lower()
    if letter == 'z':
        result_label.config(text="Nothing comes after z, pick another letter.")
        return

    # ---------- Work out the allowed range ----------
    max_shift = ord('z') - ord(letter)

    # ---------- Check the number ----------
    try:
        shift = int(text)
    except ValueError:
        result_label.config(text="Please enter a valid number.")
        return

    if not 1 <= shift <= max_shift:
        result_label.config(text=f"Please enter a number between 1 and {max_shift}.")
        return

    # ---------- Shift and show the result ----------
    new_letter = chr(ord(letter) + shift)
    result_label.config(text=f"{letter} -> {new_letter}")


# ---------- Build the window ----------
window = tk.Tk()
window.title("Caesar Shift")

tk.Label(window, text="Letter:").grid(row=0, column=0, padx=10, pady=5)
letter_entry = tk.Entry(window, width=5)
letter_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(window, text="Shift:").grid(row=1, column=0, padx=10, pady=5)
number_entry = tk.Entry(window, width=5)
number_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Button(window, text="Shift", command=shift_letter).grid(
    row=2, column=0, columnspan=2, pady=10
)

result_label = tk.Label(window, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

window.mainloop()