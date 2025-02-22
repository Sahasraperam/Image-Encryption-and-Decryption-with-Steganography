
---

# 🖼️ Image Encryption & Decryption with Steganography 🔐

Welcome to the **Image Encryption & Decryption with Steganography** project! 🎉 This tool allows you to securely encrypt and decrypt images using AES encryption and hide sensitive information inside images using **Least Significant Bit (LSB)** steganography. 🔒

Whether you want to secure your images or secretly send messages inside pictures, this is the perfect solution. Just upload your image, choose a password, and let the magic happen! 🎩✨

---

## 🚀 Features:

- **🔐 AES Encryption**: Strong encryption for securing your images with a password.
- **💻 LSB Steganography**: Hide encrypted data inside images (you won’t see it, but it’s there! 👀).
- **📸 Decrypting Images**: Easily decrypt the hidden image data using the correct password.
- **✨ Image Encryption & Decryption**: Upload an image, encrypt it, and save it with hidden data.
- **🌟 Automatic Image Viewer**: The decrypted image opens automatically once decrypted—no more hassle!

---

## ⚡ How to Use:

### 1. **Encrypt Image:**

- 💼 **Step 1**: Click the **"Encrypt and Hide Image"** button.
- 🔐 **Step 2**: Choose an image from your computer. 📸
- 🛠️ **Step 3**: Enter a strong password to encrypt your image. 🔑
- 💾 **Step 4**: Save the newly encrypted image with hidden data! 🗝️

### 2. **Decrypt Image:**

- 📂 **Step 1**: Click the **"Decrypt and Reveal Image"** button.
- 🔑 **Step 2**: Select the encrypted image you want to decrypt.
- 🧩 **Step 3**: Enter the correct password (the one used during encryption).
- 📸 **Step 4**: Voila! The decrypted image will open automatically! 😎

---

## 🔧 Requirements:

- Python 3.x 🐍
- Pillow (PIL) for image handling 🖼️
- Cryptography library for AES encryption 🔒
- Stegano library for hiding and revealing hidden messages 🕵️‍♂️

### 🛠️ Install Required Libraries:

You can install the necessary libraries using `pip`:

```bash
pip install pillow cryptography stegano
```

---

## 🌟 How It Works:

### 1. **AES Encryption**:
We use **AES (Advanced Encryption Standard)** to encrypt the image data using a password you provide. AES is a secure encryption algorithm used worldwide to keep data safe. 🔐

### 2. **LSB Steganography**:
Once the image is encrypted, we hide the encrypted data within the image using **LSB (Least Significant Bit)** steganography. It’s a way of encoding data inside the image without visually altering it. 🤫

### 3. **Decryption**:
To decrypt the image, you simply need to provide the correct password. The encrypted data will be revealed from the image and decrypted back into its original form. 🧩

---

## 🧑‍💻 Example:

1. **Encryption Example**:

   - You have an image (e.g., `beach.jpg`). 🏖️
   - You provide a password (e.g., `my_secret_password123`). 🔑
   - The image will be encrypted and saved as `beach.png` (with hidden data inside it).
   - This encrypted image can now be shared securely with anyone who knows the password.

2. **Decryption Example**:

   - The recipient receives `beach.png` with the hidden encrypted data.
   - They provide the password (`my_secret_password123`) and the image is decrypted and opened automatically. 🌈

---

## 💡 Tips:

- 🔑 **Strong Passwords**: Use a strong and unique password to make your encryption more secure.
- 🌍 **Image Formats**: This tool supports **PNG**, **JPEG**, and **JPG** image formats for encryption.
- 🕵️‍♂️ **Steganography Fun**: You can hide secret messages inside your images! For example, you can secretly store important text files inside pictures. 📄🎨

---

## ⚠️ Warnings:

- 🚨 If you lose the password, there's no way to decrypt the image! So make sure to save it somewhere safe.
- 📉 If the image you try to decrypt doesn't have hidden data, the tool will show an error: "No hidden message found in the image." 🛑

---

## 📸 Screenshots:

![Encrypting Image](![image](https://github.com/user-attachments/assets/aeb54335-39c9-4f0b-abd7-e3d456797532)
)
![image](https://github.com/user-attachments/assets/f985aa71-fd5d-40ac-bc57-3388747d0597)

*Encrypt your image by selecting a file and entering a password.*

![Decrypting Image](![image](https://github.com/user-attachments/assets/e0fbd505-be88-4c07-b9b7-38f15688b27b)
)
*Decrypt your encrypted image by selecting the encrypted file and entering the correct password.*

---

## 📜 License:

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 📄

---

## 🙋‍♂️ Need Help?

Feel free to open an issue or contact me if you have any questions or need help using this tool. I’m happy to assist! 😃

---

## 📧 Contact Me:

If you have any suggestions or issues, please feel free to reach out to me!

- 📩 **Email**: [your.email@example.com](mailto:sahasra.peram.77@gmail.com)
- 💼 **LinkedIn**: [linkedin.com/in/your-profile](https://www.linkedin.com/in/sahasra-peram/)

---

## 🎉 Enjoy the Project!

Happy encrypting, decrypting, and hiding secret messages in your images! 🎨🔐

---

### How to Add Screenshots:
1. Save screenshots of the application in the `images/` folder of your project directory.
2. Update the `![Encrypting Image](./images/encrypt_image.png)` and `![Decrypting Image](./images/decrypt_image.png)` sections with the path to your images.

---

Feel free to update the **Contact** and **Screenshots** sections with your personal details and images! Let me know if you need further modifications or help! 😊
