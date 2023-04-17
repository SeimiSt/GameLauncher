# Import the required libraries
from tkinter import *
from PIL import ImageTk, Image
import subprocess
#define functions for opening games
def open_pingpong():
      subprocess.Popen(["python", "C:/Users/lorzi/Documents/Schule/FSST_Walch/Games_Launcher/Code/pingpong.py"])

def open_tictactoe():
      subprocess.Popen(["python", "C:/Users/lorzi/Documents/Schule/FSST_Walch/Games_Launcher/Code/tictactoe.py"])

# Create an instance of Tkinter Frame
win = Tk()
win.title("Arcade Games Launcher")

# Set the geometry of Tkinter Frame
win.geometry("1920x1080")

# Open the Image File
bg = ImageTk.PhotoImage(Image.open("bgimg.ppm").resize((1920, 1080), Image.ANTIALIAS))

# Create a Canvas
canvas = Canvas(win, width=700, height=3500)
canvas.pack(fill=BOTH, expand=True)

# Add Image inside the Canvas
canvas.create_image(0, 0, image=bg, anchor='nw')

# Function to resize the window
def resize_image(e):
   global image, resized, image2
   # open image to resize it
   image = Image.open("bgimg.ppm")
   # resize the image with width and height of root
   resized = image.resize((e.width, e.height), Image.ANTIALIAS)

   image2 = ImageTk.PhotoImage(resized)
   canvas.create_image(0, 0, image=image2, anchor="nw")

# Bind the function to configure the parent window
win.bind("<Configure>", resize_image)
#create button to open tic tac toe
btn_ttt = Button(win, text = 'Tic Tac Toe', bd = '5',font=("Arcade Interlaced", 20), bg="#ab23ff", command=open_tictactoe)
btn_ttt.place(x=200, y=550)
#create button to open ping pong
btn_pp = Button(win, text = "Ping Pong", bd = "5",font=("Arcade Interlaced", 20), bg="#ab23ff", command=open_pingpong)
btn_pp.place(x=1080, y=550)
#create label for the title
title=Label(win, bd="5", font=("Arcade Interlaced", 40), bg="#ab23ff", text="ARCADE GAMES LAUNCHER")
title.place(x=240, y=200)
win.mainloop()