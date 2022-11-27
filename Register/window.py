from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("350x500")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 500,
    width = 350,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    175.0, 250.0,
    image=background_img)


############################################################################
entry0 = Entry(
    bd = 0,
    bg = "#F4F8FA",
    #bg="blue",
    foreground="#414D55",
    highlightthickness = 0,
    font = ("Roboto-Bold", int(12)))


entry0.place(
    x = 42, y = 125,
    width = 260,
    height = 22)

############################################################################
entry1 = Entry(
    bd = 0,
    bg = "#F4F8FA",
    foreground="#414D55",
    highlightthickness = 0,
    font = ("Roboto-Bold", int(12)))


entry1.place(
    x = 42, y = 202,
    width = 260,
    height = 22)

############################################################################
entry2 = Entry(
    bd = 0,
    bg = "#F4F8FA",
    foreground="#414D55",
    highlightthickness = 0,
    font = ("Roboto-Bold", int(12)))


entry2.place(
    x = 42, y = 280,
    width = 225,
    height = 22)

############################################################################
entry3 = Entry(
    bd = 0,
    bg = "#F4F8FA",
    foreground="#414D55",
    highlightthickness = 0,
    font = ("Roboto-Bold", int(12)))


entry3.place(
    x = 42, y = 357,
    width = 225,
    height = 22)


##################################################################################

SingIn = PhotoImage(file = f"SingIn.png")
SingIn_Button = Button(
    image = SingIn,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

SingIn_Button.place(
    x = 256, y = 53,
    width = 60,
    height = 22)

##################################################################################

Eye = PhotoImage(file = f"Eye.png")
Eye_Button = Button(
    image = Eye,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

Eye_Button.place(
    x = 274, y = 265,
    width = 15,
    height = 17)

##################################################################################
Create_acc = PhotoImage(file = f"Create_acc.png")
Create_acc_Button = Button(
    image = Create_acc,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

Create_acc_Button.place(
    x = 115, y = 426,
    width = 120,
    height = 17)


window.resizable(False, False)
window.mainloop()
