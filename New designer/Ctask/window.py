from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("580x400")
window.configure(bg = "#f4f4f4")
canvas = Canvas(
    window,
    bg = "#f4f4f4",
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

#######################################################################
Number = Entry(
    bd = 0,
    bg = "#F4F4F4",
    #bg="blue",
    foreground="#696D6E",
    highlightthickness = 0,
    font = ("Roboto-Bold", int(8)))


Number.place(
    x = 93, y = 69,
    width = 178,
    height = 25)

Number.focus()

#######################################################################
Name = Entry(
    bd = 0,
    bg = "#F4F8FA",
    #bg="blue",
    foreground="#696D6E",
    highlightthickness = 0,
    font = ("Roboto-Bold", int(8)))


Name.place(
    x = 80, y = 130,
    width = 192,
    height = 25)

#######################################################################
Log = Text(
    bd = 0,
    bg = "#F4F8FA",
    #bg="blue",
    foreground="#696D6E",
    highlightthickness = 0,
    font = ("Roboto-Bold", int(8)))


Log.place(
    x = 304, y = 68,
    width = 240,
    height = 86)
#######################################################################

CtaskLabel1 = StringVar()
CtaskLabel1 = 'ctask2510500'

canvas.create_text(
    92,245,
    fill="white",  
    font="Roboto 9",
    text=CtaskLabel1)
#######################################################################

CtaskLabel2 = StringVar()
CtaskLabel2 = 'ctask2510500'

canvas.create_text(
    92,292,
    fill="white",  
    font="Roboto 9",
    text=CtaskLabel2)

#######################################################################

CtaskLabel3 = StringVar()
CtaskLabel3 = 'ctask2510500'

canvas.create_text(
    92,340,
    fill="white",  
    font="Roboto 9",
    text=CtaskLabel3)



#######################################################################
Ctask1 = Entry(
    bd = 0,
    bg = "#F4F4F4",
    #bg="green",
    foreground="#696D6E",
    highlightthickness = 0,
    font = ("Roboto-Bold", int(8)))


Ctask1.place(
    x = 140, y = 232,
    width = 313,
    height = 28)



#######################################################################
Ctask2 = Entry(
    bd = 0,
    #bg = "#F4F8FA",
    bg="blue",
    foreground="#696D6E",
    highlightthickness = 0,
    font = ("Roboto-Bold", int(14)))


Ctask2.place(
    x = 140, y = 279,
    width = 313,
    height = 28)

#######################################################################
Ctask3 = Entry(
    bd = 0,
    #bg = "#F4F8FA",
    bg="blue",
    foreground="#696D6E",
    highlightthickness = 0,
    font = ("Roboto-Bold", int(14)))


Ctask3.place(
    x = 140, y = 326,
    width = 313,
    height = 28)

#######################################################################
Total = StringVar()
Total = 'Total'

canvas.create_text(
    521,311,
    fill="#28B5E1",
    font="Roboto 16 bold",
    text=Total)

#######################################################################
Numero = StringVar()
Numero = '0'

canvas.create_text(
    539,345,
    fill="#28B5E1",
    font="Roboto 21 bold",
    text=Numero)

window.resizable(False, False)
window.mainloop()
