#!python3
# Volume Calculator
# Feel free to rename your variables


import math
def menu():
    input("For The Volume Of A Square Enter: '1'\n For The Area Of A Square Enter: '2'\n For The Volume Of A Rectangle Enter: '3'\n For The Area Of A Rectangle Enter: '4'\n For The Volume Of A Sphere Enter: '5'\n For The Area Of A Sphere Enter: '6'\n For Sales Tax Enter: '7'\n For Canadian To AMerican Currency Exchange Enter: '8'\n ")
    if input==1:
        volume_of_sqaure
    elif input==2:
        area_of_sqaure
    elif input==3:
        volume_of_rectangle
    elif input==4:
        area_of_rectangle
    elif input==5:
        volume_of_sphere
    elif input==6:
            area_of_sphere
    elif input==7:
        calcTax
    elif input==8:
        usd_to_cad
    elif input==9:
        print("Goodbye")
pass



def volume_of_sphere():
    r = input("enter a radius")
    return  4/3 * math.pi * r**3


def area_of_sphere():
    r = input("enter a radius")
    return 4* math.pi *r**2

def area_of_sqaure():
    x=input
    ttal=x**2
    print(ttal)
    return ttal
def volume_of_sqaure():
    x = int(input("enter a length "))
    final=x**3
    print("The Volume is",final)
 

def volume_of_rectangle():
    L = input("enter a length ")
    W = input("enter a wides ")
    H = input("enter a height ")
    return L*W*H

def area_of_rectangle():
    L = input("enter a length ")
    W = input("enter a wides ")
    return W * L



def usd_to_cad(value):
 value=input('Enter Amount In USD')
 return value*1.37
    
 
pass
def calcTax():
    x=input("Enter Product Price Before Tax")
    tax=x*0.12
    total=x+tax
    print("Amount Of Taxes{tax}. Total Amount",total)
    return total


<<<<<<< Updated upstream
menu()
=======


menu()

>>>>>>> Stashed changes
