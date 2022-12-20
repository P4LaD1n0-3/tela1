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

##########################################################################

Change_ctask = Entry(
    bd = 0,
    bg="#F4F4F4",
    highlightthickness = 0)

Change_ctask.place(
    x = 100.0, y = 77,
    width = 180.0,
    height = 26)

##########################################################################

Req_ritm = Entry(
    bd = 0,
    bg="#F4F4F4",
    highlightthickness = 0)

Req_ritm.place(
    x = 100.0, y = 154,
    width = 180.0,
    height = 26)

##########################################################################

send_to = Entry(
    bd = 0,
    bg="#F4F4F4",
    highlightthickness = 0)

send_to.place(
    x = 90.0, y = 229,
    width = 194.0,
    height = 26)

##########################################################################

copia1 = Entry(
    bd = 0,
    bg="#F4F4F4",
    highlightthickness = 0)

copia1.place(
    x = 90.0, y = 304,
    width = 194.0,
    height = 26)

##########################################################################

copia2 = Entry(
    bd = 0,
    bg="#F4F4F4",
    highlightthickness = 0)

copia2.place(
    x = 90.0, y = 379,
    width = 194.0,
    height = 26)


##########################################################################

file = Entry(
    bd = 0,
    bg="#F4F4F4",
    highlightthickness = 0)

file.place(
    x = 362.0, y = 379,
    width = 170.0,
    height = 26)


##########################################################################

Log = Entry(
    bd = 0,
    bg="#F4F4F4",
    highlightthickness = 0)

Log.place(
    x = 320.0, y = 78,
    width = 495.0,
    height = 101)

##########################################################################

EntryLog = Entry(
    bd = 0,
    bg="#F4F4F4",
    highlightthickness = 0)

EntryLog.place(
    x = 320.0, y = 230,
    width = 495.0,
    height = 101)

##########################################################################

File = PhotoImage(file = f"File.png")
FileBtn = Button(
    image = File,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

FileBtn.place(
    x = 535, y = 380,
    width = 27,
    height = 25)

window.resizable(False, False)
window.mainloop()
