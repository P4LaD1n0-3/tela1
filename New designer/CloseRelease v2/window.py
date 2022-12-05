from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("350x530")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 530,
    width = 350,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    175.0, 265.0,
    image=background_img)

#######################################################################
Release = Entry(
    bd = 0,
    bg = "#F4F8FA",
    #bg="blue",
    foreground="#696D6E",
    highlightthickness = 0,
    font = ("Roboto-Bold", int(14)))


Release.place(
    x = 90, y = 110,
    width = 210,
    height = 25)

Release.focus()

#######################################################################
Log = Text(
    bd = 0,
    #bg = "#F4F8FA",
    bg="blue",
    foreground="#696D6E",
    highlightthickness = 0,
    font = ("Roboto-Bold", int(14)))


Log.place(
    x = 30, y = 190,
    width = 290,
    height = 230)

#######################################################################
Encerrar = PhotoImage(file = f"Encerrar.png")
BtnEncerrar = Button(
    image = Encerrar,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

BtnEncerrar.place(
    x = 245, y = 477,
    width = 70,
    height = 20)

#######################################################################
Cancelar = PhotoImage(file = f"Cancelar.png")
BtnCancelar = Button(
    image = Cancelar,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

BtnCancelar.place(
    x = 136, y = 477,
    width = 70,
    height = 20)


window.resizable(False, False)
window.mainloop()
