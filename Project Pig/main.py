from fns import fetch_image, store_images, turn, disp_score, roller, store, dices
from customtkinter import CTk, CTkLabel, CTkButton, CTkImage
from PIL import Image

'''Initial Values'''
dice_images = store_images(dices)

# Tkinter window
app = CTk()
app.title("Pig Game")
window_width = 800
window_height = int(window_width * (3 / 4))
app.geometry(f"{window_width}x{window_height}")
app.resizable(False, False)

background_image = fetch_image('https://i.ibb.co/Dr8PLsz/pig-1.jpg')
background_image = background_image.resize((window_width, window_height), Image.LANCZOS)
app.background_photo = CTkImage(background_image, size=(window_width, window_height))
background_label = CTkLabel(app, image=app.background_photo, text="")
background_label.place(x=0, y=0, relwidth=1, relheight=1)

turn_label = turn(app)
turn_label.place(x=590, y=50)
temp_score = CTkLabel(app, text="0", font=("Times New Roman", 52), bg_color='#FAF4E5', fg_color='#BB6A4E', width=100, height=50)
temp_score.place(x=350, y=200)

m1, m2 = disp_score(app)
m1.place(x=100, y=400)
m2.place(x=550, y=400)

roll_btn = CTkButton(master=app, text="Roll", font=("Arial", 14), corner_radius=8, fg_color="#5F2E15", bg_color="#512611", hover_color="brown", border_color="#512611", border_width=0, width=50, height=20, command=lambda: roller(temp_score, turn_label, dice_images))
dice_btn = CTkButton(master=app, text="Store", font=("Arial", 14), corner_radius=8, fg_color="#5F2E15", bg_color="#512611", hover_color="brown", border_color="#512611", border_width=0, width=50, height=20, command=lambda: store(app, temp_score, m1, m2, turn_label))
roll_btn.place(x=300, y=400)
dice_btn.place(x=450, y=400)

app.mainloop()
