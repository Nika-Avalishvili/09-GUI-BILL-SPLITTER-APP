import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk

# საწყისი ცვლადები
bill_amount = 0.00
bill_tip = 0.00
bill_people = 1.00

# ბექი



def selected_tip(rate):
    global bill_tip, bill_amount, bill_people

    bttn_dict = {'5': bttn1,
                '10': bttn2,
                '15': bttn3,
                '25': bttn4,
                '50': bttn5}

    if type(rate) != int:
        rate = bttn6.get()
        for (key, value) in bttn_dict.items():
            bttn_dict[key]['state']='active'
    else:
        bttn6.delete(0,'end')
        for (key, value) in bttn_dict.items():
            if key != str(rate):
                bttn_dict[key]['state']='active'
            else:
                bttn_dict[key]['state']='disabled'

    if rate == '':
        rate = 0

    bill_tip = bill_amount * float(rate) / 100


def people_number(event):
    global bill_people, bill_tip, bill_amount

    bill_amount = float(bill_inp.get())
    bill_people = float(people_inp.get())

    if bill_people == 0:
        people_num_check.config(text = "Can't be 0!", font = ('Courier',11), fg='red')

    tip_per_person = bill_tip / bill_people
    total_per_person = (bill_amount + bill_tip) / bill_people
    tip_amount3.config(text = f'  ${round(tip_per_person,2):.2f}')
    total_amount3.config(text = f'  ${round(total_per_person,2):.2f}')



def clear_func(event):
    global bill_amount, bill_tip, bill_people
    bill_amount = 0.00
    bill_tip = 0.00
    bill_people = 1.00

    bttn_dict = {'5': bttn1,
                '10': bttn2,
                '15': bttn3,
                '25': bttn4,
                '50': bttn5}

    bttn6.delete(0,'end')
    bill_inp.delete(0,'end')
    people_inp.delete(0,'end')
    tip_amount3.config(text = '  $0.00')
    total_amount3.config(text = '  $0.00')
    for (key, value) in bttn_dict.items():
        bttn_dict[key]['state']='active'



# ვიზუალური ინტერფეისი
window = tk.Tk()

window.title("Bill Splitter")
window.resizable(width=True,height=True)
window.geometry("700x500")
window.configure(bg='#b9dee1')

title = tk.Label(window, text = "BILL SPLITTER", font = ('Courier',36), bg='#b9dee1', fg = "#2f5453")
title.pack(pady = 30)

frame = tk.Frame(window, borderwidth = 0, bg = 'white', padx = 30, pady = 30)
frame.config(width = 300, height = 150)
frame.config(relief = 'flat')
frame.pack()

bill = tk.Label(frame, text = "Bill", font = ('Courier',14), bg='white').grid(row = 0, column = 0, columnspan = 3, sticky = 'w')
bill_inp = tk.Entry(frame, highlightthickness=2, width = 20, font = ('Courier',18), relief='flat', highlightbackground="#f2f8f9", highlightcolor="#27b89d", bg = "#f2f8f9")
bill_inp.grid(row = 1, column = 0, columnspan = 3, sticky = 'w')
# bill_inp.insert(0, "0")
bill_inp.bind('<KeyRelease>',people_number)
bill_inp.bind('<Leave>',people_number)

bill_type = tk.Label(frame, text = "Select Tip %", font = ('Courier',14), bg='white').grid(row = 4, column = 0, columnspan = 3, sticky = 'w')

bttn1 = tk.Button(frame, text = "5%", activebackground = '#91e4d8', activeforeground = '#093639', highlightthickness=0, font = ('Courier',16), fg = 'white', highlightcolor="red", highlightbackground='#093639', bg = "#093639", width = 4, height = 1, relief='flat', borderwidth=0, command = lambda rate = 5 : selected_tip(rate))
bttn1.grid(row = 5, column = 0, padx = (0,5), pady = 5, sticky = 'w')

bttn2 = tk.Button(frame, text = "10%", activebackground = '#91e4d8', activeforeground = '#093639', highlightthickness=0, font = ('Courier',16), fg = 'white', highlightcolor="red", highlightbackground='#093639', bg = "#093639", width = 4, height = 1, relief='flat', borderwidth=0, command = lambda rate = 10 : selected_tip(rate))
bttn2.grid(row = 5, column = 1, padx = 5, pady = 5,)

bttn3 = tk.Button(frame, text = "15%", activebackground = '#91e4d8', activeforeground = '#093639', highlightthickness=0, font = ('Courier',16), fg = 'white', highlightcolor="red", highlightbackground='#093639', bg = "#093639", width = 4, height = 1, relief='flat', borderwidth=0, command = lambda rate = 15 : selected_tip(rate))
bttn3.grid(row = 5, column = 2, padx = (5,20), pady = 5, sticky = 'e')

bttn4 = tk.Button(frame, text = "25%", activebackground = '#91e4d8', activeforeground = '#093639', highlightthickness=0, font = ('Courier',16), fg = 'white', highlightcolor="red", highlightbackground='#093639', bg = "#093639", width = 4, height = 1, relief='flat', borderwidth=0, command = lambda rate = 25 : selected_tip(rate))
bttn4.grid(row = 6, column = 0, padx = (0,5), pady = 5, sticky = 'w')

bttn5 = tk.Button(frame, text = "50%", activebackground = '#91e4d8', activeforeground = '#093639', highlightthickness=0, font = ('Courier',16), fg = 'white', highlightcolor="red", highlightbackground='#093639', bg = "#093639", width = 4, height = 1, relief='flat', borderwidth=0, command = lambda rate = 50 : selected_tip(rate))
bttn5.grid(row = 6, column = 1, padx = 5, pady = 5,)

bttn6 = tk.Entry(frame, text = "Custom", highlightthickness=2, width = 7, font = ('Courier',13), relief='flat', highlightbackground="#f2f8f9", highlightcolor="#27b89d", bg = "#f2f8f9")
bttn6.grid(row = 6, column = 2, padx = (5,20), pady = 5, sticky = 'we')
# bttn6.insert(0, "Custom")
bttn6.bind('<KeyRelease>',selected_tip)
bttn6.bind('<Leave>',selected_tip)

people_num = tk.Label(frame, text = "Number of People", font = ('Courier',14), bg='white').grid(row = 8, column = 0, columnspan = 2, sticky = 'w')
people_num_check = tk.Label(frame, font = ('Courier',14), bg='white')
people_num_check.grid(row = 8, column = 2, sticky = 'w')



people_inp = tk.Entry(frame, highlightthickness=0.5, width = 20, font = ('Courier',18), relief='flat', highlightbackground="#f2f8f9", highlightcolor="#27b89d", bg = "#f2f8f9")
# people_inp.insert(0, "0")
people_inp.grid(row = 9, column = 0, columnspan = 3, sticky = 'w')


# user_icon = PhotoImage(file='download.png')
# people_inp.config(image = user_icon)

people_inp.bind('<KeyRelease>', people_number)
people_inp.bind('<Leave>', people_number)


frame_sec = tk.Frame(frame, borderwidth=20, background="red", relief='flat', bg='#093639')
frame_sec.config(pady = 20, padx = 20)
frame_sec.grid(row = 0, rowspan = 10, column = 3, sticky = "NSE")

tip_amount1 = tk.Label(frame_sec, text = "Tip Amount", font = ('Courier',14), fg = '#cdd4d5', bg='#093639').grid(row = 0, column = 0, sticky = 'ws')
tip_amount2 = tk.Label(frame_sec, text = "/ person", font = ('Courier',10), fg = "#516a6c", bg='#093639').grid(row = 1, column = 0, sticky = 'wn')

tip_amount3 = tk.Label(frame_sec, text = "  $0.00", font = ('Courier',30), fg="#27b89d", bg='#093639')
tip_amount3.grid(row = 0, rowspan = 2, column = 2, sticky = 'e')

total_amount1 = tk.Label(frame_sec, text = "Total", font = ('Courier',14), fg = '#cdd4d5', bg='#093639').grid(row = 2, column = 0, sticky = 'ws')
total_amount2 = tk.Label(frame_sec, text = "/ person", font = ('Courier',10), fg = "#516a6c", bg='#093639').grid(row = 3, column = 0, sticky = 'wn')

total_amount3 = tk.Label(frame_sec, text = "  $0.00", font = ('Courier',30), fg="#27b89d", bg='#093639')
total_amount3.grid(row = 2, rowspan = 2, column = 2, sticky = 'w')

interval = tk.Label(frame_sec, bg='#093639', text = '', font = ('Courier',72)).grid(row = 5, rowspan = 2, column = 0, columnspan = 3, sticky = 's')
bttn7 = tk.Button(frame_sec, text = "RESET", highlightthickness=0.5, font = ('Courier',16), relief='groove', highlightbackground="#27b89d", borderwidth = 0)
bttn7.grid(row = 9, column = 0, columnspan = 3, sticky = 'swe')
bttn7.bind("<Button-1>",clear_func)


window.mainloop()
