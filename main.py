# Import the necessary libraries
import base64
from PIL import Image

# Open the image file
with Image.open('image.png') as image:
  # Convert the image to a list of pixel values
  pixels = list(image.getdata())
  # Encode the message as a base64 string
  message = base64.b64encode(b'my secret message')
  # Convert the message to a list of integers
  message_pixels = [int(x) for x in message]
  # Replace the least significant bit of each pixel with a bit from the message
  encoded_pixels = [(r & ~1) | (m & 1) for (r, g, b), m in zip(pixels, message_pixels)]
  # Create a new image with the encoded pixels
  encoded_image = Image.new(image.mode, image.size)
  encoded_image.putdata(encoded_pixels)
  # Save the encoded image
  encoded_image.save('encoded_image.png')
