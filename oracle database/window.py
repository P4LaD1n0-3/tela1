from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("580x400")
window.configure(bg = "#FFFFFF")
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 400,
    width = 580,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    290.0, 200.0,
    image=background_img)

window.resizable(False, False)
window.mainloop()
