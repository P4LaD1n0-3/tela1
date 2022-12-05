from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("580x400")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 400,
    width = 580,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    286.5, 190.0,
    image=background_img)


################################################################

Change = Entry(
    window,
    bd = 0,
    #bg = "#F4F8FA",
    bg="blue",
    foreground="#696D6E",
    highlightthickness = 0,
    font = ("Roboto-Bold", int(10)))


Change.place(
    x = 95, y = 60,
    width = 150,
    height = 22)

Change.focus()


################################################################

Req = Entry(
    window,
    bd = 0,
    #bg = "#F4F8FA",
    bg="blue",
    foreground="#696D6E",
    highlightthickness = 0,
    font = ("Roboto-Bold", int(10)))

Req.place(
    x = 95, y = 122,
    width = 150,
    height = 22)

################################################################

Send_to = Entry(
    window,
    bd = 0,
    #bg = "#F4F8FA",
    bg="blue",
    foreground="#696D6E",
    highlightthickness = 0,
    font = ("Roboto-Bold", int(10)))

Send_to.place(
    x = 85, y = 185,
    width = 180,
    height = 22)

################################################################

Copia1 = Entry(
    window,
    bd = 0,
    #bg = "#F4F8FA",
    bg="blue",
    foreground="#696D6E",
    highlightthickness = 0,
    font = ("Roboto-Bold", int(10)))


Copia1.place(
    x = 85, y = 244,
    width = 180,
    height = 22)

################################################################

Copia2 = Entry(
    window,
    bd = 0,
    #bg = "#F4F8FA",
    bg="blue",
    foreground="#696D6E",
    highlightthickness = 0,
    font = ("Roboto-Bold", int(10)))


Copia2.place(
    x = 85, y = 322,
    width = 180,
    height = 22)

################################################################
Log = Text(
    window,
    bd = 0,
    #bg = "#F4F8FA",
    bg="blue",
    foreground="#696D6E",
    highlightthickness = 0,
    font = ("Roboto-Bold", int(10)))


Log.place(
    x = 304, y = 58,
    width = 230,
    height = 86)    
    

################################################################
EntryText = Text(
    window,
    bd = 0,
    #bg = "#F4F8FA",
    bg="blue",
    foreground="#696D6E",
    highlightthickness = 0,
    font = ("Roboto-Bold", int(10)))


EntryText.place(
    x = 304, y = 182,
    width = 230,
    height = 86) 

################################################################

File_Text = Text(
    window,
    bd = 0,
    #bg = "#F4F8FA",
    bg="blue",
    foreground="#696D6E",
    highlightthickness = 0,
    font = ("Roboto-Bold", int(10)))


File_Text.place(
    x = 335, y = 322,
    width = 92,
    height = 20)

################################################################


Confirm = PhotoImage(file = f"Confirm.png")
BtnConfirm = Button(
    window,
    image = Confirm,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

BtnConfirm.place(
    x = 478, y = 281,
    width = 58,
    height = 20)


################################################################


Send = PhotoImage(file = f"Send.png")
BtnSend = Button(
    window,
    image = Send,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

BtnSend.place(
    x = 492, y = 321,
    width = 35,
    height = 17)


################################################################

File = PhotoImage(file = f"File.png")
BtnFile = Button(
    window,
    image = File,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

BtnFile.place(
    x = 430, y = 320,
    width = 23,
    height = 20)

window.resizable(False, False)
window.mainloop()
