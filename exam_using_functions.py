#21/10/2024
#Assginment of operators
#caluculate rate of interest
def interest(p,t,r):
    r=p*t*r/100
    print("total ammnt:",r)
#convert celsius to ferheint
def ferheint(c):
    f=(9/5)*c+32
    print(f)
#area and perimeter of a reactangle
def cal_rect(l,w):
    a=l*w
    p=2*(l+w)
    print(a)
    print(p)
#write a python to compute spead using s=ut+1/2at2 using functions
def compute_spead(u,a,t):
    s=u*t+0.5*(a*t*t)
    print(s)