from PIL import Image
import numpy as np

def encrypt_pixel(pixel):
    return (pixel ** 2) % 3233

def encrypt_image(input_path, output_path):
    img = Image.open(input_path).convert("L")
    pixels = np.array(img)

    encrypted_pixels = np.vectorize(encrypt_pixel)(pixels)
    encrypted_pixels = encrypted_pixels % 256

    encrypted_img = Image.fromarray(encrypted_pixels.astype('uint8'))
    encrypted_img.save(output_path)

    print("Image encrypted successfully")

if __name__ == "__main__":
    encrypt_image("sample.png", "encrypted.png")
