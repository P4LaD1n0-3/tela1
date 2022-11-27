from tkinter import *
from datetime import datetime

def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("900x500")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 500,
    width = 900,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    450.0, 250.0,
    image=background_img)


Dml = PhotoImage(file = f"Dml.png")

Dml_Button = Button(
    image= Dml,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    bg="white",
    relief = "flat")

Dml_Button.place(
    x = 95, y = 204,
    width = 35,
    height = 15)

Ebao = PhotoImage(file = f"Ebao.png")

Ebao_Button = Button(
    image= Ebao,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    bg="white",
    )

Ebao_Button.place(
    x = 96, y = 235,
    width = 40,
    height = 12)


Portal = PhotoImage(file = f"Portal.png")

Portal_Button = Button(
    image= Portal,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    bg="white",
    )

Portal_Button.place(
    x = 96, y = 263,
    width = 47,
    height = 14)


Contacts = PhotoImage(file = f"Contacts.png")

Contacts_Button = Button(
    image= Contacts,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    bg="white",
    )

Contacts_Button.place(
    x = 95, y = 295,
    width = 65,
    height = 11)


About = PhotoImage(file = f"About.png")

About_Button = Button(
    image= About,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    bg="white",
    )

About_Button.place(
    x = 92, y = 324,
    width = 49,
    height = 13)


Manager = PhotoImage(file = f"Manager.png")

Manager_Button = Button(
    image= Manager,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    bg="white",
    )

Manager_Button.place(
    x = 95, y = 354,
    width = 65,
    height = 14)


########################################################################################
#today = day()

day = StringVar()
day = '27'

canvas.create_text(
    406,318,
    fill="#28B5E1",
    font="Arial 20 bold",
    text=day)

########################################################################################
#today = day()

Month_year = StringVar()
Month_year = 'September 2019'

canvas.create_text(
    520,330,
    fill="#28B5E1",
    font="Arial 12 bold",
    text=Month_year)

########################################################################################
#today = day()

Day_Month_year = StringVar()
Day_Month_year = 'Monday, September 22'

canvas.create_text(
    696,179,
    fill="#414D55",
    font="Arial 10 bold",
    text=Day_Month_year)

########################################################################################
#today = day()


Welcome = 'Welcome'

canvas.create_text(
    640,86,
    fill="#414D55",
    font="Arial 14 bold",
    text=Welcome)

########################################################################################
#today = day()

Name = StringVar()
Name = 'West Jackeline'

canvas.create_text(
    708,118,
    fill="#28B5E1",
    font="Arial 11 bold",
    text=Name)

########################################################################################
#today = day()

Profile = StringVar()
Profile = 'Sallie Butler'

canvas.create_text(
    700,140,
    fill="#414D55",
    font="Arial 11 bold",
    text=Profile)

########################################################################################
#today = day()

Hours = StringVar()
Hours = '47'

canvas.create_text(
    390,96,
    fill="#414D55",
    font="Arial 26 bold",
    text=Hours)

########################################################################################
#today = day()

Minuts = StringVar()
Minuts = '47'

canvas.create_text(
    390,186,
    fill="#414D55",
    font="Arial 26 bold",
    text=Minuts)

########################################################################################
#today = day()

Secounds = StringVar()
Secounds = '161'

canvas.create_text(
    505,96,
    fill="#414D55",
    font="Arial 26 bold",
    text=Secounds)

########################################################################################
#today = day()

Miles = StringVar()
Miles = '161'

canvas.create_text(
    505,186,
    fill="#414D55",
    font="Arial 26 bold",
    text=Miles)


window.resizable(False, False)
window.mainloop()
