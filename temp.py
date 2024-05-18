'''if you are running for the first time then go to line 17 and uncomment that function to install requirements'''
import socket
import subprocess
import sys

def install_req():
    try:
        # Attempt to connect to a well-known website
        socket.create_connection(("www.google.com", 80))  # just checking for internet
        req = ['pillow', 'requests', 'customtkinter', 'numpy', 'playsound']
        subprocess.run(['pip', 'install'] + req)
        print('\033[2J\033[H', end='') 
    except OSError:
        print("\033[91mError: Not connected to the internet.\033[0m")
        sys.exit(1)

# Uncomment this line if running for the first time to install requirements
# install_req()

print('\033[2J\033[H', end='') 
import tkinter as tk
from PIL import Image, ImageTk
from playsound import playsound

def player(file):
    playsound(file)

def show(image_path, title="Image", size=(400, 400), position=(0, 0)):
    root = tk.Tk()
    root.title(title)
    img = Image.open(image_path)
    img = img.resize(size, Image.LANCZOS) 
    img = ImageTk.PhotoImage(img)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{size[0]}x{size[1]}+{screen_width - size[0]}+{position[1]}")
    root.attributes("-topmost", True)
    label = tk.Label(root, image=img)
    label.pack()
    def keep_on_top():
        root.attributes("-topmost", True)
        root.after(100, keep_on_top)
    # keep_on_top()
    root.after(1, lambda: root.focus_force())
    root.after(1, lambda: root.lift())
    root.after(1, lambda: root.update())
    root.update()
    return root, img

'''Project logic starts here
All the above contents are from ChatGPT'''
print('\033[96mPlayer Registration\033[0m')
player_name = input('name :')

msg = f"\033[93mDora and {player_name.capitalize()} set out on a thrilling adventure today. As they journeyed through the wilderness, their path led them to a weathered bridge with some missing pieces. So you, {player_name}, have to fix the bridge.\033[0m "
print(msg, end='')

# Task 2
root, img = show('Project 4/bridge.jpg', 'fix the bridge')
while True:
    try:
        gaps = int(input('How many gaps can you see? : '))
        if gaps == 7:
            player('Project 4/bridge.wav')
            print('Congratulations you fixed the bridge!', end='')
            root.destroy()
            break
        elif gaps == 0:
            root.destroy()
            print('You were afraid to continue your adventure, you ran away!')
            break
        elif gaps < 7:
            print(f'You are wrong: {7-gaps} gaps remaining! ')
            root.destroy()
            break
        elif gaps > 7:
            print(f'You are wrong: only 7 gaps, time to test your eyes', end='\n\n\n')
            root.destroy()
            break
    except ValueError:
        print('\033[91mInvalid Entry\033[0m  Let`s try again', end='\t')

# Task 3
print('The journey continues...')
root, img = show('Project 4/map.jpg', 'map')
print(f'Hey {player_name}, I kind of lost my way. Look at the map. Which way do we have to go, left or right?')
while True:
    try:
        player('Project 4/left.wav')
        direction = input('Which way should we go? (left/right): ').lower()
        if direction == 'left':
            print('Ok, let’s go!')
            player('Project 4/Ramani.wav')
            root.destroy()
            break
        elif direction == 'right':
            root.destroy()
            print('You fool, I cannot swim! You led me to a river.')
            print('\033[91mDora died\033[0m')
            break
        else:
            root.destroy()
            print('We lost the way completely.')
            print('\033[93mGoing back\033[0m')
            break
    except Exception:
        print('\033[91mInvalid Entry\033[0m  Let’s try again', end='\t')
