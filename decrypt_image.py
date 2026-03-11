from PIL import Image
import numpy as np

def decrypt_pixel(pixel):
    return int(pow(pixel,0.5)) % 256

def decrypt_image(input_path, output_path):
    img = Image.open(input_path).convert("L")
    pixels = np.array(img)

    decrypted_pixels = np.vectorize(decrypt_pixel)(pixels)
    decrypted_img = Image.fromarray(decrypted_pixels.astype('uint8'))
    decrypted_img.save(output_path)

    print("Image decrypted successfully")

if __name__ == "__main__":
    decrypt_image("encrypted.png", "decrypted.png")
