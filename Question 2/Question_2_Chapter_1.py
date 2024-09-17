import time 
from PIL import Image
import numpy as np
import os

#Step one: Process the number 'n'
current_time = int(time.time())
generated_number = (current_time % 100) + 50
if generated_number % 2 == 0:
    generated_number += 10
print("Generated Number (n):", generated_number)

#finding out the image
image_location = "pic\chapter.jpg"


#Replacing the path of image through file
image = Image.open(image_location)


#conversion of image to the array
image_array = np.array(image)

#placing 'n' in equal to associated pixel's RGB
modified_image_array = image_array + generated_number

#Ensuring that these are inside the valid RGB range (0-255)
modified_image_array = np.clip(modified_image_array, 0, 255)

#Converting the modified array to an image
modified_image = Image.fromarray(modified_image_array.astype('uint8'))

#Save the modified image in a specific location
output_image_location = 'pic\m.jpg'
modified_image.save(output_image_location)

#final formation of the modified image
modified_image.show()

