#!python3
# Volume Calculator
# Feel free to rename your variables


import math
def menu():
    x = int(input("For The Volume Of A Square Enter: '1'\n For The Area Of A Square Enter: '2'\n For The Volume Of A Rectangle Enter: '3'\n For The Area Of A Rectangle Enter: '4'\n For The Volume Of A Sphere Enter: '5'\n For The Area Of A Sphere Enter: '6'\n For Sales Tax Enter: '7'\n For Canadian To AMerican Currency Exchange Enter: '8'\n "))
    if x==1:
        volume_of_sqaure()
    elif x==2:
        area_of_sqaure()
    elif x==3:
        volume_of_rectangle()
    elif x==4:
        area_of_rectangle()
    elif x==5:
        volume_of_sphere()
    elif x==6:
            area_of_sphere()
    elif x==7:
        calcTax()
    elif x==8:
        usd_to_cad()
    elif x==9:
        print("Goodbye")
pass



def volume_of_sphere():
    r = int(input("enter a radius"))
    return  4/3 * math.pi * r**3


def area_of_sphere():
    r = int(input("enter a radius"))
    area =  4* math.pi *r**2
    print(area)
    return area

def area_of_sqaure():
    x=int(input("enter a aside"))
    ttal=x**2
    print(ttal)
    return ttal

def volume_of_sqaure():
    x = int(input("enter a length "))
    final=x**3
    print("The Volume is",final)
    return final
 

def volume_of_rectangle():
    L = int(input("enter a length "))
    W = int(input("enter a wides "))
    H = int(input("enter a height "))
    return L*W*H

def area_of_rectangle():
    L = int(input("enter a length "))
    W = int(input("enter a wides "))
    return W * L



def usd_to_cad():
    c=int(input('Enter Amount In USD'))
    tootal=c*1.37
    print(tootal)
    

def calcTax():
    x=int(input("Enter Product Price Before Tax"))
    tax=x*0.12
    total=x+tax
    print("Amount Of Taxes{tax}. Total Amount",total)
    return total


menu()

