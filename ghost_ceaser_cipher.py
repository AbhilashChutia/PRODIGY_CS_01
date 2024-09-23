import tkinter as tk

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def encrypt_message():
    message = message_text.get("1.0", "end-1c")  # Get text from Text widget
    shift_value = int(shift_entry.get())
    encrypted_message = encrypt(message, shift_value)
    result_text.delete("1.0", tk.END)  # Clear previous result
    result_text.insert(tk.END, encrypted_message)  # Insert encrypted message into result text widget

def decrypt_message():
    message = message_text.get("1.0", "end-1c")  # Get text from Text widget
    shift_value = int(shift_entry.get())
    decrypted_message = decrypt(message, shift_value)
    result_text.delete("1.0", tk.END)  # Clear previous result
    result_text.insert(tk.END, decrypted_message)  # Insert decrypted message into result text widget

window = tk.Tk()
window.title("Ghost: A Caesar Cipher Tool")

tk.Label(window, text="Enter the message:").grid(row=0, column=0, padx=10, pady=10)
message_text = tk.Text(window, height=5, width=50)
message_text.grid(row=0, column=1, padx=10, pady=10)

tk.Label(window, text="Enter the shift value:").grid(row=1, column=0, padx=10, pady=10)
shift_entry = tk.Entry(window, width=5)
shift_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

button_frame = tk.Frame(window)
button_frame.grid(row=2, column=0, columnspan=2, pady=10)

encrypt_button = tk.Button(button_frame, text="Encrypt", command=encrypt_message, width=15)
encrypt_button.pack(side="left", padx=5)

decrypt_button = tk.Button(button_frame, text="Decrypt", command=decrypt_message, width=15)
decrypt_button.pack(side="right", padx=5)

tk.Label(window, text="Result:").grid(row=3, column=0, padx=10, pady=10)
result_text = tk.Text(window, height=5, width=50)
result_text.grid(row=3, column=1, padx=10, pady=10)

window.mainloop()
