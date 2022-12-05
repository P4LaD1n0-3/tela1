from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("350x400")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 400,
    width = 350,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    175.0, 200.0,
    image=background_img)

############################################################################
#Data log
entry0 = Entry(
    bd = 0,
    bg = "#F4F8FA",
    foreground="#414D55",
    highlightthickness = 0,
    font = ("Roboto-Bold", int(12)))


entry0.place(
    x = 46, y = 118,
    width = 260,
    height = 22)


entry1 = Entry(
    bd = 0,
    bg = "#F4F8FA",
    foreground="#414D55",
    highlightthickness = 0,
    font = ("Roboto-Bold", int(12)))

entry1.place(
    x = 46, y = 218,
    width = 230,
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
    x = 280, y = 210,
    width = 15,
    height = 15)


##################################################################################

Login = PhotoImage(file = f"Login.png")
Login_Button = Button(
    image = Login,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

Login_Button.place(
    x = 75, y = 302,
    width = 46,
    height = 25)



##################################################################################


Register = PhotoImage(file = f"Register.png")
Register_Button = Button(
    image = Register,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

Register_Button.place(
    x = 210, y = 305,
    width = 60,
    height = 23)



window.resizable(False, False)
window.mainloop()
