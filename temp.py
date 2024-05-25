from customtkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO
import random

''' Initial Values for the game '''
# Dice image list
dl = [
    'https://i.ibb.co/rMg6Cvk/image.png',
    'https://i.ibb.co/dcKyhyr/1.jpg',
    'https://i.ibb.co/k2VJHL3/2.jpg',
    'https://i.ibb.co/cQ2Fry9/3.jpg',
    'https://i.ibb.co/jvFJv0t/4.jpg',
    'https://i.ibb.co/QMftx7z/5.jpg',
    'https://i.ibb.co/sgbKb4r/6.jpg'
]
dice = 0
players = {
    1: 0,
    2: 0
}
actv = 1

# functions
def roll():
    global dice
    dice = random.randint(1, 6)

def fetch_image(url):
    response = requests.get(url)
    image_data = response.content
    return Image.open(BytesIO(image_data))

def place_image_center(root, image_url):
    # Fetch and resize the background image
    background_image = fetch_image('https://i.ibb.co/Dr8PLsz/pig-1.jpg')
    window_width = 800
    window_height = int(window_width * (3 / 4))
    background_image = background_image.resize((window_width, window_height), Image.LANCZOS)
    root.background_photo = CTkImage(background_image, size=(window_width, window_height))

    # Create a label to display the background image
    background_label = CTkLabel(root, image=root.background_photo, text="")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Fetch the center image
    center_image = fetch_image(image_url)

    # Calculate the scaling factor to fit the image within the desired dimensions
    width_ratio = 50 / center_image.width
    height_ratio = 50 / center_image.height
    scaling_factor = min(width_ratio, height_ratio)

    # Resize the image with the calculated scaling factor
    center_image = center_image.resize((int(center_image.width * scaling_factor), int(center_image.height * scaling_factor)), Image.LANCZOS)
    root.center_photo = CTkImage(center_image, size=(int(center_image.width * scaling_factor), int(center_image.height * scaling_factor)))

    # Calculate center position for the center image
    center_x = (window_width - center_image.width) // 2
    center_y = (window_height - center_image.height) // 2

    # Create a label to display the center image
    center_label = CTkLabel(root, image=root.center_photo, text="")
    center_label.place(x=center_x, y=center_y)

app = CTk()
app.title("4:3 Aspect Ratio Window")

window_width = 800
window_height = int(window_width * (3 / 4))
app.geometry(f"{window_width}x{window_height}")
app.resizable(False, False)
background_image_url = 'https://i.ibb.co/Dr8PLsz/pig-1.jpg'
place_image_center(app, dl[0])  # ready

title_label = CTkLabel(app, text=f'P{actv}`s turn', font=("Helvetica", 16), text_color="white", fg_color=None)
title_label.place(x=350, y=200)

# The Game Section:

app.mainloop()
