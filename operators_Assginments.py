#21/10/2024
#Operators assginment
#caluculate rate of interest
p=input("enter ammnt")
t=input("enter time")
r=input("enter rate ")
i=p*t*r/100
print("total amount:",i)
#write a program using to compute area and perimeter for
#area=l*w
#p=2*(l+w)
l=int(input("enter the length of the rectriangle:"))
w=int(input("enter the wedth of the rectriangle:"))
area=l*w
print("area of the rectriangle of length",l,"and wiedth",w,"is:",area)
perimeter=2*(l+w)
print("perimeter of the rectriangle of length",l,"and wiedth",w,"is:",perimeter)
#write a python program to convert celsius to farenheit
#forula:f=(9/5)*c+32
c=int(input("enter value of c:"))
f=(9/5)*c+32
print("conversion of celsius to farenheit is:",f)
#write a python to compute spead using s=ut+1/2at2 using functions
def compute_spead(u,a,t):
    s=u*t+0.5*(a*t*t)
    print(s)
