import os
import sys
import socket
import subprocess
from io import BytesIO
import random
from PIL import Image
import requests
from customtkinter import CTkLabel, CTkImage

def install_req():
    print('\033[2J\033[H', end='')
    print('\033[96mAttention as we are using some external libraries in our code - we have to install them first ,this will require Internet connection !\033[0m')
    v=input (f'to Continue Enter any key \n\t\t to Exit  \033[91m[x]\033[0m: ')
    try:
        # Attempt to connect to a well-known website
        socket.create_connection(("www.google.com", 80))  #just checking for internet
        req = ['pillow','requests','customtkinter']
        if(v=='x' or v=='X'):
            print('\033[2J\033[H', end='Opted Not to Install')
            return None
        subprocess.run(['pip', 'install'] + req)
        print('\033[2J\033[H', end='') 
    except OSError:
        print("\033[91mError: Not connected to the internet.\033[0m")
        sys.exit(1)

# Install required packages
install_req()
print('\033[2J\033[H', end='')
rules=''' \033[96mGame Rules \033[0m
\033[91m-\033[0m The game is for two players.
\033[91m-\033[0m Players take turns to roll a  die.
\033[91m-\033[0m On a turn, a player can roll the die as many times as they wish.
\033[91m-\033[0m Each number rolled is added to temporary score.
\033[91m-\033[0m as the temporary score increses player has to choose between wheather he has to become greedy or store at right time
\033[91m-\033[0m If a player rolls a 1, they loose all the score they collected in temporary score.
\033[91m-\033[0m If a player rolls any other number, it is added to their turn total and they can choose to roll again or store.
\033[91m-\033[0m If a player chooses to hold, their turn total is added to their score.
\033[91m-\033[0m The first player to reach or exceed 50 points wins the game.

Once you read the rules the game will start!
'''
print(rules)

# Initial Values for the game
dices = [
    'https://i.ibb.co/rMg6Cvk/image.png',
    'https://i.ibb.co/dcKyhyr/1.jpg',
    'https://i.ibb.co/k2VJHL3/2.jpg',
    'https://i.ibb.co/cQ2Fry9/3.jpg',
    'https://i.ibb.co/jvFJv0t/4.jpg',
    'https://i.ibb.co/QMftx7z/5.jpg',
    'https://i.ibb.co/sgbKb4r/6.jpg'
]
dice = 0
players = {1: 0, 2: 0}
actv = 1
temp = 0

def fetch_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = response.content
        return Image.open(BytesIO(image_data))
    except requests.RequestException as e:
        print(f"Error fetching image from {url}: {e}")
        return None
    
p1=fetch_image('https://i.ibb.co/kKPkkLj/Art-Lab-com-ist-artlab-Fri-May-24-15-54-17-GMT-05-30-2024.png')
p2=fetch_image('https://i.ibb.co/xDqgmFH/Art-Lab-com-ist-artlab-Fri-May-24-15-55-18-GMT-05-30-2024.png')

def victory(app, actv):
    if actv == 1:
        background_image = p1
    else:
        background_image = p2
    if background_image is not None:
        window_width = app.winfo_screenwidth()
        window_height = app.winfo_screenheight()
        background_image = background_image.resize((window_width, window_height), Image.LANCZOS)
        background_photo = CTkImage(background_image, size=(window_width, window_height))

        # Create a label to display the background image
        background_label = CTkLabel(app, image=background_photo, text="")
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.lift()

def store_images(urls):
    images = []
    for url in urls:
        img = fetch_image(url)
        if img:
            images.append(img)
        else:
            images.append(None)
    return images

def roll():
    global dice
    dice = random.randint(1, 6)

def show_dice(root, img):
    if img is None:
        return

    window_width = 800
    window_height = int(window_width * (3 / 4))
    width_ratio = 50 / img.width
    height_ratio = 50 / img.height
    scaling_factor = min(width_ratio, height_ratio)

    new_width = int(img.width * scaling_factor)
    new_height = int(img.height * scaling_factor)
    img = img.resize((new_width, new_height), Image.LANCZOS)
    root.center_photo = CTkImage(img, size=(new_width, new_height))

    center_x = (window_width - new_width) // 2
    center_y = (window_height - new_height) // 2

    center_label = CTkLabel(root, image=root.center_photo, text="")
    center_label.place(x=center_x, y=center_y)

def turn(root):
    img = fetch_image('https://i.ibb.co/khDWRvs/Art-Lab-com-ist-artlab-Wed-May-22-21-52-22-GMT-05-30-2024.jpg')
    if img is None:
        return None

    width_ratio = 160 / img.width
    height_ratio = 90 / img.height
    scaling_factor = min(width_ratio, height_ratio)
    new_width = int(img.width * scaling_factor)
    new_height = int(img.height * scaling_factor)
    img = img.resize((new_width, new_height), Image.LANCZOS)
    root.turn_photo = CTkImage(img, size=(new_width, new_height))

    turn_label = CTkLabel(root, image=root.turn_photo, text="")
    return turn_label

def disp_score(root):
    img1 = fetch_image('https://i.ibb.co/nbB19k0/M1.png')
    img2 = fetch_image('https://i.ibb.co/GJ2R6H0/M2.png')
    if img1 is None or img2 is None:
        return None, None

    width_ratio = 160 / img1.width
    height_ratio = 90 / img1.height
    scaling_factor = min(width_ratio, height_ratio)
    new_width = int(img1.width * scaling_factor)
    new_height = int(img1.height * scaling_factor)

    img1 = img1.resize((new_width, new_height), Image.LANCZOS)
    img2 = img2.resize((new_width, new_height), Image.LANCZOS)

    root.m1_photo = CTkImage(img1, size=(new_width, new_height))
    m1 = CTkLabel(root, image=root.m1_photo, text="0", font=("Arial", 22))

    root.m2_photo = CTkImage(img2, size=(new_width, new_height))
    m2 = CTkLabel(root, image=root.m2_photo, text="0", font=("Arial", 22))

    return m1, m2

def store(app, scr, m1, m2, x):
    global temp
    global actv
    players[actv] += temp
    if players[actv] >= 50:
        victory(app, actv)

    temp = 0
    scr.configure(text="0")
    if actv == 1:
        m1.configure(text=str(players[1]))
        actv = 2
        x.place(x=100, y=50)
    else:
        m2.configure(text=str(players[2]))
        actv = 1
        x.place(x=590, y=50)

def roller(scr, x, dice_images):
    global temp
    global actv
    roll()
    show_dice(scr, dice_images[dice])
    if dice == 1:
        temp = 0
        scr.configure(text='out')
        turnX = 100 if actv == 1 else 590
        x.place(x=turnX, y=50)
        actv = 1 if actv == 2 else 2
    else:
        temp += dice
        scr.configure(text=str(temp))
