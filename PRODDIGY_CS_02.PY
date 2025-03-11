from PIL import Image

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()

    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            pixels[i, j] = (r ^ key, g ^ key, b ^ key)  # XOR operation

    encrypted_path = "encrypted_image.png"
    img.save(encrypted_path)
    print(f"Encrypted image saved as {encrypted_path}")

def decrypt_image(image_path, key):
    encrypt_image(image_path, key)  # XOR operation again restores original

key = 42  # Any numeric key for encryption
encrypt_image("input.png", key)
decrypt_image("encrypted_image.png", key)
