'''if you are running I`st time then go to line 16 and uncomment that function in order to install requirments'''
import socket
import subprocess
import sys
def install_req():
    try:
        # Attempt to connect to a well-known website
        socket.create_connection(("www.google.com", 80))  #just checking for internet
        req = ['pillow', 'requests', 'customtkinter','numpy']
        subprocess.run(['pip', 'install'] + req)
        print('\033[2J\033[H', end='') 
        # print('\033[96m' + 'Loading GUI, please wait...' + '\033[0m')
    except OSError:
        print("\033[91mError: Not connected to the internet.\033[0m")
        sys.exit(1)
# install_req()    #if running for first time run this
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
    keep_on_top()
    root.after(1, lambda: root.focus_force())
    root.after(1, lambda: root.lift())
    root.after(1, lambda: root.update())
    root.update()
    return root, img








'''Project logic starts here
All the above contents are from chatgpt'''
print('\033[96mPlayer Registration\033[0m')
player_name=input('name :')

msg=f"\033[93mDora and {player_name.capitalize()} set out on a thrilling adventure today.As they journeyed through the wilderness, their path led them to a weathered bridge with some missing pieces.so you {player_name} has to fix the bridge \033[0m "
print(msg,end='')

# task 1
root, img = show('Project 4/bridge.jpg','fix the bridge')
while True:
    try:
        gaps = int(input('How many gaps can you see? : '))
        if gaps == 7:
            player('Project 4/bridge.wav')
            print('Congratulations you fixed the bridge!',end='')
            root.destroy()
            break
        elif gaps==0:
            root.destroy()
            print('You were afraid to continue your adventure, you ran away!')
            break
        elif gaps < 7:
            print(f'You are Wrong: {7-gaps} gaps Remaining! ')
            root.destroy()
            break
        elif gaps > 7:
            print(f'You are Wrong: only 7 gaps time to test your eyes ',end='\n\n\n')
            root.destroy()
            break
    except ValueError:
        print('\033[91mInvalid Entry\033[0m  Let`s try again',end='\t')

# task 2
print('the Journey continues...')
root, img = show('Project 4/map.jpg','map')
print(f'hey {player_name} kind of lost my way,look at the map which way we have to go ,left or right ?')
while True:
    try:
        direction = input('How many gaps can you see? : ').lower()
        if direction == 'left':
            player('Project 4/left.wav')
            print('ok lets go !')
            root.destroy()
            break
        elif direction== 'right':
            root.destroy()
            print('You fool i cannot swim you lead me to a river ')
            print('\033[91mDora died\033[0m')
            break
        else:
            root.destroy()
            print('we lost the way completly ')
            print('\033[93mGoing back\033[0m')
            break
    except Exception:
        print('\033[91mInvalid Entry\033[0m  Let`s try again',end='\t')
