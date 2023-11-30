import easyocr
import os
import numpy as np
from PIL import Image

folder_path = "/home/maruf/Downloads/Verti"

# EasyOCR Reader instance
reader = easyocr.Reader(['en'])

#  serial number
serial_number = 1

# ----------------------------------Link limit ------------------------Link limit ------------------------Link limit ------------------------Link limit --------------------
result_limit = 200

# Iterate through files in the folder
for filename in os.listdir(folder_path):
    if serial_number > result_limit:
        print(f"Total images {result_limit}")
        break

    image_path = os.path.join(folder_path, filename)

    if os.path.isfile(image_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        # Open the image
        image = Image.open(image_path)

        # Convert the PIL.Image.Image to a numpy array
        image_np = np.array(image)

        # Catch text from the image
        results = reader.readtext(image_np)

        # Extracted text from the image
        extracted_text = ' '.join([result[1] for result in results])

        # Print the result of all text found in the image
        print(f"Image Path: {image_path}:\n{extracted_text}\n")

        # Increment serial number
        serial_number += 1
