import numpy as np
from PIL import Image#pillow library being used to open manipulate save images

def load_image(image_path):
    img = Image.open(image_path)
    img_array = np.array(img) #converting the image into an numpy array
    return img_array

def encrypt_image(img_array, key):
    encrypted_array = img_array.copy()
    height, width, _ = img_array.shape

    for i in range(height):
        for j in range(width):
            encrypted_array[i, j] = img_array[i, j] ^ key  

    return encrypted_array

def decrypt_image(encrypted_array, key):
    return encrypt_image(encrypted_array, key)  #XORing again

def main():
    image_path = input("Enter the path to the image: ").strip()
    key = 128  
    img_array = load_image(image_path)
    encrypted_array = encrypt_image(img_array, key)
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_image.save('encrypted_image.png')
    print("Encrypted image saved as 'encrypted_image.png'")
    decrypted_array = decrypt_image(encrypted_array, key)
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_image.save('decrypted_image.png')
    print("Decrypted image saved as 'decrypted_image.png'")
main()
