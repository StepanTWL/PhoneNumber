import tkinter as tk
from sys import platform
from tkinter import ttk
import tkinter.font as font

"""
if platform == "win32":
    from win32api import GetSystemMetrics
    from ctypes  import *
    print(windll.user32.GetSystemMetrics(0))
    print(windll.user32.GetSystemMetrics(1))
elif platform == "darwin":
    # OS X
"""

def pi(length : int) -> str:
    pi = ''
    reminders = [2]*length*10//3
    heldDigits = 0#временно недействительные цифры

    for i in range(length):
        carriedOver = 0
        sum = 0
        for j in range(length*10//3,-1,-1):
            reminders[j] *= 10
            sum = reminders[j] + carriedOver
            quotient = sum//(j*2+1)
            reminders[j] = sum % (j*2+1)
            carriedOver = quotient*j

        reminders[0] = sum % 10
        q = sum // 10
        if q == 9:
            heldDigits += 1
        elif q == 10:
            q = 0
            for k in range(1,heldDigits+1):
                replaced = int(pi[i-k])
                if replaced == 9:
                    replaced = 0
                else:
                    replaced += 1
                pi[i-k]=str(replaced)
            heldDigits = 1
        else:
            heldDigits = 1
        pi += str(q)
    return pi


constant = ('pi', 'fi', 'e', 'sqr(2)', 'sqr(3)')

window = tk.Tk()
window.geometry(f'300x400+500+200')#size - 300x400, indent - 500x200
window.title('My Phone Number')
window.resizable(width=False, height=False)#conts size

combo = ttk.Combobox(window, values=constant, font = ('Arial', 10, 'bold'))#select math const
combo.grid(row=1,column=1,pady=10,padx=10)#raslopojenie
combo.current(0)#default first math const

#myFont = font.Font(family='Arial', size=16, weight='bold')
start = tk.Button(window, text='Start', font = ('Arial', 15, 'bold'))
start.grid(row=2,column=1,sticky='we',padx=10, pady=10)

number=tk.Entry(window, justify=tk.RIGHT, font=('Arial', 15, 'bold'), width=7)#prijimaetsya vpravo, max dlina 7 simvolov
number.insert(0,'000-00-00')#0 pri zapuske
number.grid(row=0, column=1,sticky='we',padx=10, pady=10)#columnspan=4(объеденяет 4 столбца)
numberLable = tk.Label( window, text='Phone Number',
                        #bg='red',
                        fg='black',
                        font=('Arial',10,'bold'),
                        padx=12,
                        #pady=40,
                        width=10,
                        #height=10,
                        anchor='w',#прижать к северу
                        #relief=tk.RAISED,#объем кнопки
                        #bd=3,#размер объема
                        justify=tk.LEFT
                        )#выравнивание
constLable = tk.Label(window, text='Math constant', font=('Arial',10,'bold'), padx=12, width=10, anchor='w', justify=tk.LEFT)
numberLable.grid(row=0, column=0)
constLable.grid(row=1, column=0)

window.mainloop()