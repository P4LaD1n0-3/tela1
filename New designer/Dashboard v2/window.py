from tkinter import *
from datetime import datetime

def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1024x568")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 568,
    width = 1024,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)


background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
     512.0, 284.0,
    image=background_img)

########################################################################################
Welcome = 'Welcome'

canvas.create_text(
    80,40,
    fill="#414D55",
    font="Arial 14 bold",
    text=Welcome)

########################################################################################

Dashboard = 'Dashboard'

canvas.create_text(
    120,75,
    fill="#28B5E1",
    font="Roboto 26",
    text=Dashboard)

########################################################################################


Name = StringVar()
Name = 'WR'

canvas.create_text(
    912,88,
    fill="#414D55",
    font="Roboto 22 bold",
    text=Name)

########################################################################################
Name = StringVar()
Name = 'Wesley Rolim'

canvas.create_text(
    914,178,
    fill="#414D55",
    font="Roboto 16 bold",
    text=Name)
########################################################################################
Name = StringVar()
Name = 'Technical Profile'

canvas.create_text(
    916,202,
    fill="#414D55",
    font="Roboto 11 bold",
    text=Name)


########################################################################################
#today = day()

Day_Month_year = StringVar()
Day_Month_year = 'Monday, September 22'

canvas.create_text(
    920,231,
    fill="#414D55",
    font="Arial 10 bold",
    text=Day_Month_year)

window.resizable(False, False)
window.mainloop()
