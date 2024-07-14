from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = np.array(image, dtype=np.uint16)  # Use uint16 to avoid overflow during addition
    
    encrypted_pixels = (pixels + key) % 256
    encrypted_image = Image.fromarray(encrypted_pixels.astype('uint8'))
    encrypted_image.save(output_path)

def decrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = np.array(image, dtype=np.uint16)  # Use uint16 to avoid overflow during subtraction
    
    decrypted_pixels = (pixels - key) % 256
    decrypted_pixels = np.clip(decrypted_pixels, 0, 255).astype('uint8')
    decrypted_image = Image.fromarray(decrypted_pixels)
    decrypted_image.save(output_path)

def main():
    choice = input("Do you want to (E)ncrypt or (D)ecrypt an image? ").strip().upper()
    if choice not in ['E', 'D']:
        print("Invalid choice. Please choose 'E' to encrypt or 'D' to decrypt.")
        return
    
    image_path = input("Enter the path of the image: ").strip()
    output_path = input("Enter the path to save the output image: ").strip()
    key = int(input("Enter a key (integer value): ").strip())
    
    if choice == 'E':
        encrypt_image(image_path, output_path, key)
        print("Image encrypted and saved to", output_path)
    elif choice == 'D':
        decrypt_image(image_path, output_path, key)
        print("Image decrypted and saved to", output_path)

if __name__ == "__main__":
    main()
