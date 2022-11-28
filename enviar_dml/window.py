from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("573x381")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 381,
    width = 573,
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
    bd = 0,
    bg = "#F4F8FA",
    foreground="#696D6E",
    highlightthickness = 0,
    font = ("Roboto-Bold", int(10)))


Change.place(
    x = 100, y = 97,
    width = 150,
    height = 22)

Change.focus()
################################################################

Send_to = Entry(
    bd = 0,
    bg = "#F4F8FA",
    foreground="#696D6E",
    highlightthickness = 0,
    font = ("Roboto-Bold", int(10)))

Send_to.place(
    x = 85, y = 166,
    width = 180,
    height = 22)

################################################################

Copia1 = Entry(
    bd = 0,
    bg = "#F4F8FA",
    foreground="#696D6E",
    highlightthickness = 0,
    font = ("Roboto-Bold", int(10)))


Copia1.place(
    x = 85, y = 235,
    width = 180,
    height = 22)

################################################################

Copia2 = Entry(
    bd = 0,
    bg = "#F4F8FA",
    foreground="#696D6E",
    highlightthickness = 0,
    font = ("Roboto-Bold", int(10)))


Copia2.place(
    x = 85, y = 312,
    width = 180,
    height = 22)

################################################################
Log = Text(
    bd = 0,
    bg = "#F4F8FA",
    foreground="#696D6E",
    highlightthickness = 0,
    font = ("Roboto-Bold", int(10)))


Log.place(
    x = 304, y = 80,
    width = 230,
    height = 40)    
    

################################################################
EntryText = Entry(
    bd = 0,
    #bg = "#F4F8FA",
    bg="blue",
    foreground="#696D6E",
    highlightthickness = 0,
    justify='left',
    font = ("Roboto-Bold", int(10)))


EntryText.place(
    x = 304, y = 165,
    width = 230,
    height = 90,
    
    ) 




################################################################

File_Text = Text(
    bd = 0,
    bg = "#F4F8FA",
    foreground="#696D6E",
    highlightthickness = 0,
    font = ("Roboto-Bold", int(10)))


File_Text.place(
    x = 335, y = 312,
    width = 92,
    height = 22)

################################################################


Confirm = PhotoImage(file = f"Confirm.png")
BtnConfirm = Button(
    image = Confirm,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

BtnConfirm.place(
    x = 477, y = 272,
    width = 58,
    height = 20)


################################################################


Home = PhotoImage(file = f"Home.png")
BtnHome = Button(
    image = Home,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

BtnHome.place(
    x = 480, y = 312,
    width = 54,
    height = 20)


################################################################

File = PhotoImage(file = f"File.png")
BtnFile = Button(
    image = File,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

BtnFile.place(
    x = 428, y = 312,
    width = 23,
    height = 20)

window.resizable(False, False)
window.mainloop()
