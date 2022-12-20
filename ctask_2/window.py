from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("850x450")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 450,
    width = 850,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    425.0, 225.0,
    image=background_img)

window.resizable(False, False)
window.mainloop()
