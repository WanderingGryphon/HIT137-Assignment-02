import os
import time
from PIL import Image


# Set input and output
input_file = 'chapter1.jpg'
output_file = 'chapter1out.png'

# Check if the input file exists
if not os.path.isfile(input_file):
    print(f"Error: File '{input_file}' does not exist.")

# Check if the output directory exists, create it if not
output_dir = os.path.dirname(output_file)
if output_dir and not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate the number based on the current time
generated_number = (int(time.time()) % 100) + 50
if generated_number % 2 == 0:
    generated_number += 10
print(f"The generated number is {generated_number}")

# Load and convert the image to RGB
chapter1 = Image.open(input_file).convert('RGB')
pixels = chapter1.load()

n = generated_number

# Modify each pixel and calculate the sum of all red pixels simultaneously
sum_new_r = 0
for i in range(chapter1.width):
    for j in range(chapter1.height):
        r, g, b = pixels[i, j]

        # Adjust pixel values with wrapping around 256
        r = (r + n) % 256
        g = (g + n) % 256
        b = (b + n) % 256

        pixels[i, j] = (r, g, b)
        sum_new_r += r

# Save the new image
chapter1.save(output_file)
print(f"Image saved to {output_file}")
print(f"Sum of all new red pixels: {sum_new_r}")
