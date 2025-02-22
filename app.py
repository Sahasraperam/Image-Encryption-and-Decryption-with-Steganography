import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import os
from stegano import lsb

class SteganographyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image Encryption and Decryption with Steganography")
        self.geometry("600x500")
        self.resizable(False, False)
        self.config(bg="#2c3e50")
        
        # Title label
        self.title_label = tk.Label(self, text="Image Encryption & Decryption with Steganography", font=("Arial", 16), fg="#ecf0f1", bg="#2c3e50")
        self.title_label.pack(pady=20)

        # Password label
        self.password_label = tk.Label(self, text="Enter encryption password:", font=("Arial", 12), fg="#ecf0f1", bg="#2c3e50")
        self.password_label.pack(pady=5)

        # Password entry
        self.password_entry = tk.Entry(self, width=45, font=("Arial", 12), bd=3, show="*")
        self.password_entry.pack(pady=5)

        # Encrypt button
        self.encrypt_button = tk.Button(self, text="Encrypt and Hide Image", font=("Arial", 12), bg="#16a085", fg="white", bd=0, width=30, command=self.encrypt_image)
        self.encrypt_button.pack(pady=20)

        # Decrypt button
        self.decrypt_button = tk.Button(self, text="Decrypt and Reveal Image", font=("Arial", 12), bg="#e74c3c", fg="white", bd=0, width=30, command=self.decrypt_image)
        self.decrypt_button.pack(pady=20)

    def encrypt_image(self):
        password = self.password_entry.get()
        if not password:
            messagebox.showerror("Error", "Password cannot be empty")
            return

        # Select image to encrypt
        image_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if not image_path:
            return

        # Read image as bytes
        with open(image_path, "rb") as image_file:
            image_bytes = image_file.read()

        # Encrypt the image
        encrypted_image = self.encrypt_data(image_bytes, password)

        # Convert encrypted image data to a hex string
        encrypted_data_str = encrypted_image.hex()

        # Hide encrypted data in image using Steganography (LSB method)
        encrypted_image_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Image", "*.png")])
        if not encrypted_image_path:
            return
        
        self.hide_data_in_image(image_path, encrypted_data_str, encrypted_image_path)

        messagebox.showinfo("Success", "Image encrypted and hidden successfully!")

    def encrypt_data(self, data, password):
        key = self.derive_key(password)
        cipher = Cipher(algorithms.AES(key), modes.CBC(b'\x00' * 16), backend=default_backend())
        encryptor = cipher.encryptor()

        # Pad the data to be a multiple of block size (16 bytes)
        padded_data = data + (16 - len(data) % 16) * b'\x00'
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

        return encrypted_data

    def derive_key(self, password):
        # Derive a 32-byte key from the password using SHA256
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(password.encode())
        return digest.finalize()

    def hide_data_in_image(self, image_path, encrypted_data_str, output_image_path):
        # Use Steganography LSB method to hide data in image
        try:
            secret_image = lsb.hide(image_path, encrypted_data_str)
            secret_image.save(output_image_path)  # Save the image with hidden data
        except Exception as e:
            messagebox.showerror("Error", f"Failed to hide data in image: {e}")
            return

    def decrypt_image(self):
        password = self.password_entry.get()
        if not password:
            messagebox.showerror("Error", "Password cannot be empty")
            return

        # Select image to decrypt
        encrypted_image_path = filedialog.askopenfilename(title="Select Encrypted Image", filetypes=[("PNG Image", "*.png")])
        if not encrypted_image_path:
            return

        # Extract encrypted message from the image using Steganography
        encrypted_message = lsb.reveal(encrypted_image_path)

        # Check if there is hidden data in the image
        if encrypted_message is None or encrypted_message == "":
            messagebox.showerror("Error", "No hidden message found in the image")
            return

        try:
            # Decrypt the extracted message
            decrypted_image_data = self.decrypt_data(bytes.fromhex(encrypted_message), password)

            # Save decrypted image
            decrypted_image_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Image", "*.png")])
            if not decrypted_image_path:
                return

            with open(decrypted_image_path, "wb") as decrypted_file:
                decrypted_file.write(decrypted_image_data)

            # Open the decrypted image automatically
            self.open_image(decrypted_image_path)

            messagebox.showinfo("Success", "Image decrypted and hidden message revealed!")

        except Exception as e:
            messagebox.showerror("Decryption Error", f"An error occurred during decryption: {str(e)}")

    def decrypt_data(self, encrypted_data, password):
        key = self.derive_key(password)
        cipher = Cipher(algorithms.AES(key), modes.CBC(b'\x00' * 16), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

        return decrypted_data

    def open_image(self, image_path):
        """Open the decrypted image using default image viewer"""
        try:
            image = Image.open(image_path)
            image.show()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open the image: {str(e)}")


if __name__ == "__main__":
    app = SteganographyApp()
    app.mainloop()
