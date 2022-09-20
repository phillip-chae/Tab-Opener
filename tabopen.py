#!python3
import webbrowser
import tkinter as tk
from tkinter import ttk

toGUI=tk.Tk()

#Click handle
def clickHandle(x):
    if x == "ait":
        webbrowser.open("https://cs.nyu.edu/courses/fall22/CSCI-UA.0467-001/_site/#xs1")
        webbrowser.open("https://edstem.org/us/courses/27587/discussion/")
        webbrowser.open("https://brightspace.nyu.edu/d2l/home/221970")
    if x == "top":
        webbrowser.open("https://brightspace.nyu.edu/d2l/home/226729")
        webbrowser.open("http://www.seyedkalali.com/wp-content/uploads/2016/11/A-First-Course-in-Probability-8th-ed.-Sheldon-Ross.pdf")
    if x == "alg":
        webbrowser.open("https://brightspace.nyu.edu/d2l/home/222597")
        webbrowser.open("https://marinazahara22.files.wordpress.com/2013/10/i-n-herstein-topics-in-algebra-2nd-edition-1975-wiley-international-editions-john-wiley-and-sons-wie-1975.pdf")
    if x == "iml":
        webbrowser.open("https://")
    if x == "helpdesk":
        webbrowser.open("https://nyu.service-now.com/")
        webbrowser.open("https://docs.google.com/spreadsheets/")
        webbrowser.open("https://sites.google.com/nyu.edu/helpdesk/helpdesk-staff-guide-and-training?authuser=0")
        webbrowser.open("https://docs.google.com/document/d/1zpphA_8EAscWSJFKIgSWrfFRetgiwBmUoGQplagZfE8/edit#heading=h.me439totjd08")
    if x == "print":
        webbrowser.open("https://nyu.service-now.com/")
        webbrowser.open("http://izumi.bobst.nyu.edu/print/")
    if x == "sheets":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1k5qS-t-TPmnm0ruhNGsiVn4LscNPL53n8PwEa1DnY3k/")
        webbrowser.open("https://docs.google.com/spreadsheets/d/1knD_KSA4rW6DorpGl-LoORjA90vQfDb-")
        webbrowser.open("https://docs.google.com/spreadsheets/d/10Rs1XhZFdJNnygxBsShcbjl0Kq70zU43G85jeDBjXfw/")
    toGUI.quit()


#Styling
style = ttk.Style(toGUI)
style.configure('TLabel', font = ('bold'))
style.configure('.', font = ('calibri', 14), borderwidth = '4')

#Styling parameters
ysymmetry = 50
padding = {'ipadx': 5, 'ipady': 5}

#Title/Heading
toGUI.title('Tab Opener')
heading = ttk.Label(toGUI, text='', style='Heading.TLabel')
heading.grid(column= 0, row = 0)
toGUI.geometry("270x355+10+20")


#class butparameter():
    #__init__(self):

#Buttons
#group = ["Applied Internet Technology"]
#for i in range(len(group)):
#def buttonequalize(txt, abbr, i, root=toGUI, pad = padding):
    #tempbut = ttk.Button(root, text = txt, command=lambda: clickHandle(abbr))
    #tempbut.grid(column = 1, row = i)

btn1 = ttk.Button(toGUI, width=25, text = "Applied Internet Technology", command=lambda: clickHandle("ait"))
btn1.grid(column=0, row=1, **padding)
btn2 = ttk.Button(toGUI, width=25, text = "Theory of Probability", command=lambda: clickHandle("top"))
btn2.grid(column=0, row=2, **padding)
btn3 = ttk.Button(toGUI, width=25, text = "Algebra", command=lambda: clickHandle("alg"))
btn3.grid(column=0, row=3, **padding)
btn4 = ttk.Button(toGUI, width=25, text = "Intro to Machine Learning", command=lambda: clickHandle("iml"))
btn4.grid(column=0, row=4, **padding)
btn5 = ttk.Button(toGUI, width=25, text = "Help Desk", command=lambda: clickHandle("helpdesk"))
btn5.grid(column=0, row=5, **padding)
btn6 = ttk.Button(toGUI, width=25, text = "Print Service", command=lambda: clickHandle("print"))
btn6.grid(column=0, row=6, **padding)
btn7 = ttk.Button(toGUI, width=25, text = "Victor's Sheets", command=lambda: clickHandle("sheets"))
btn7.grid(column=0, row=7, **padding)

#Backend

toGUI.mainloop()