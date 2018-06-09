import tkinter as tk

root = tk.Tk()
tk.Label(root,
		 text="Red Text in Times Font",
		 fg = "red",
		 font = "Times").pack()
tk.Label(root,
		 text="Green Text in Helvetica Font",
		 fg = "light green",
		 bg = "dark green",
		 font = "Helvetica 16 bold italic").pack()
tk.Label(root,
		 text="Blue Text in Verdana bold",
		 fg = "blue",
		 bg = "yellow",
		 font = "Verdana 10 bold").pack()

root.mainloop()
def write_slogan():
    print("Tkinter is easy to use!")

frame = tk.Frame(master)
frame.pack()

button = tk.Button(frame,
                   text="QUIT",
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Hello",
                   command=write_slogan)
slogan.pack(side=tk.LEFT)

from tkinter import *

T = Text(master, height=30, width=150)
T.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
T.pack()
T.insert(END, "Just a text Widget\nin two lines\n")
mainloop()
# from tkinter import *
#
# root = Tk()
#
# text2 = Text(root, height=20, width=50)
# scroll = Scrollbar(root, command=text2.yview)
# text2.configure(yscrollcommand=scroll.set)
# text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
# text2.tag_configure('big', font=('Verdana', 20, 'bold'))
# text2.tag_configure('color', foreground='#476042',
# 						font=('Tempus Sans ITC', 12, 'bold'))
# text2.tag_bind('follow', '<1>', lambda e, t=text2: t.insert(END, "Not now, maybe later!"))
# text2.insert(END,'\nWilliam Shakespeare\n', 'big')
# quote = """
# To be, or not to be that is the question:
# Whether 'tis Nobler in the mind to suffer
# The Slings and Arrows of outrageous Fortune,
# Or to take Arms against a Sea of troubles,
# """
# text2.insert(END, quote, 'color')
# text2.insert(END, 'follow-up\n', 'follow')
# text2.pack(side=LEFT)
# scroll.pack(side=RIGHT, fill=Y)
#
# root.mainloop()
