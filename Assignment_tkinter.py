#write a python to determine grade of student
'''from pyexpat.errors import messages
from tkinter import*
from tkinter import messagebox



window=Tk()
window.config(bg="blue")
window.geometry("350x400")

def grad():
    score=int(e1.get())
    if score >= 90:
        messagebox.showinfo("RESUL","A grede")
    elif score >= 80 and score < 90:
        messagebox.showinfo("RESULT","B grade")
    elif score >= 70 and score < 80:
        messagebox.showinfo("RESULT","C grade")
    elif score >= 60 and score < 70:
        messagebox.showinfo("RESULT","D grade")
    else:

        messagebox.showinfo("RESULT","FAIL")


l1=Label(window,text="ENTER THE SCORE:")
l1.grid(row=0,column=0)
e1=Entry(window)
e1.grid(row=0,column=1)


b1=Button(window,text="grad",command=grad)
b1.grid(row=2,column=0)


window.mainloop()'''

'''write a python program to calculate a discount for a customer  based on  the purchased amount
using tkinter
conditions:
purchase>=$500: 20% discount
purchase>=200 and <$500: 10% discount
purchase<$200: NO Disc'''
from tkinter import*
from tkinter import messagebox



window=Tk()
window.title("Discount")
window.config(bg="yellow")
window.geometry("350x400")

def discount():
    purchase=int(e1.get())
    if purchase>=500:
        messagebox.showinfo("RESULT","20 % DISCOUNT U WILL GET")
        Total_amount=purchase*0.2
    elif purchase>=200 and purchase<500:
        messagebox.showinfo("RESULT", "10% DISCOUNT U WILL GET")
        Total_amount=purchase*0.1

    else:
        messagebox.showinfo("RESULT", "no discount")
        Total_amount=purchase




l1=Label(window,text="ENTER THE AMOUNT:")
l1.grid(row=0,column=0)
e1=Entry(window)
e1.grid(row=0,column=1)

b1=Button(window,text="Discount",command=discount)
b1.grid(row=2,column=0)


window.mainloop()