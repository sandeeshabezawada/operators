#23/10/24......LOGICAl OPERATORS ASSGINMENT:
'''Write python program using tkinter to check speed of the car and give warning
penalty if the speed exceeded
speed_limit=90kmph
1.speed<=spedd_limit:no penalty
2.speed<=speed_limit+20:warning
3.speed>speed_limit+20:penalty 2000'''

'''from tkinter import*
from tkinter import messagebox

window=Tk()
window.title("vehical speed limit")
window.config(bg="yellow")
window.geometry("350x400")

def speed_limit():
    speed=int(e2.get())
    speedlmt=int(e3.get())
    if speed<=speedlmt:
        messagebox.showinfo("warning","no penalty")
    elif speed<=speedlmt+20:
        messagebox.showinfo("warning","your are crossing the speed limit")
    elif speed>speedlmt+20:
        messagebox.showinfo("warning","your get crossed the speed limit so penalty is:2000")
    else:
        messagebox.showinfo("HAPPY JURNEY")


l2=Label(window,text="Enter the speed")
l2.grid(row=0,column=0)
e2=Entry(window)
e2.grid(row=0,column=1)
l3=Label(window,text="Enter the speed limit")
l3.grid(row=2,column=0)
e3=Entry(window)
e3.grid(row=2,column=1)
b1=Button(window,text="speed caluculater",command=speed_limit)
b1.grid(row=3,column=1)


window.mainloop()'''

#2.Write a python program using tkinter for withdraw money from ATM
'''conditions:
balance=10000
daily_limit=20000
1.withdrawal amount<=balance
2.withdrawel notes should be multiples of 100
3.daily limit should not be exceeded'''

'''from tkinter import*
from tkinter import messagebox

window=Tk()
window.title("ATM")
window.config(bg="orange")
window.geometry("350x400")

def Atm_operation():
    balance=10000
    withdrawamnt=int(e1.get())
    if withdrawamnt<=balance and withdrawamnt %100==0:
        messagebox.showinfo("withdrawel","take your money and take your money in 100rs notes")

    elif withdrawamnt > balance:
        messagebox.showinfo("daily limit","your daily limit if finished")
    else:
        messagebox.showinfo("balance","total balance is")
        total_bal=withdrawamnt-balance


def check_balance():
    balance=10000
    withdrawamnt=int(e1.get())
    messagebox.showinfo("Balance",balance-withdrawamnt)


l1=Label(window,text="Enter the withdraw amnt")
l1.grid(row=0,column=0)
e1=Entry(window)
e1.grid(row=0,column=1)

b1=Button(window,text="withdraw",command=Atm_operation)
b1.grid(row=2,column=1)
b2=Button(window,text="Balance",command=check_balance)
b2.grid(row=3,column=1)


window.mainloop()'''

'''Assignment 3: 
write a python program using tkinter for checking customer
is eligible for discount or not
business condition:
inputs: purchase_amt
membership= True or False
purchase_amt>5000 or membership==True: 20% discount avail'''


from tkinter import*
from tkinter import messagebox

window=Tk()
window.title("CUSTOMER DISCOUNT")
window.config(bg="skyblue")
window.geometry("350x400")

def discount_eligibility():
    purchase_amount=int(e1.get())
    membership=True
    if purchase_amount>5000 and membership==True:
        messagebox.showinfo("discount details","you will get 20% discount")
    else:
        messagebox.showinfo("Discount details ","your not get any discount")

l1=Label(window,text="Total Purchase Amount")
l1.grid(row=0,column=0)
e1=Entry(window)
e1.grid(row=0,column=1)

b1=Button(window,text="Discount",command=discount_eligibility)
b1.grid(row=2,column=1)



window.mainloop()




