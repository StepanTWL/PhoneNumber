import tkinter as tk
from sys import platform
from tkinter import ttk

"""
if platform == "win32":
    from win32api import GetSystemMetrics
    from ctypes  import *
    print(windll.user32.GetSystemMetrics(0))
    print(windll.user32.GetSystemMetrics(1))
elif platform == "darwin":
    # OS X
"""

constant = ('pi', 'fi', 'e', 'sqr(2)', 'sqr(3)')

window = tk.Tk()
window.geometry(f'300x400+500+200')#size - 300x400, indent - 500x200
window.title('My Phone Number')
window.resizable(width=False, height=False)#conts size

combo = ttk.Combobox(window, values=constant)#select math const
combo.grid(row=0,column=0,pady=5,padx=50)#raslopojenie
combo.current(0)#default first math const

start = ttk.Button(window, text='Start')
start.grid(row=2,column=0,sticky='we',padx=50, pady=5)

number=tk.Entry(window,justify=tk.RIGHT, font=('Arial', 15), width=15)
#number.insert(0,'0')#0 pri zapuske
number.grid(row=1, column=0,columnspan=4,sticky='we',padx=50)

window.mainloop()