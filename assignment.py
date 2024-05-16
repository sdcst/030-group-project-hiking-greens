#!python3
# Volume Calculator
# Feel free to rename your variables


import math
def menu():
    while True:
        x = input(" For The Volume Of A Square Enter: '1'\n For The Area Of A Square Enter: '2'\n For The Volume Of A Rectangle Enter: '3'\n For The Area Of A Rectangle Enter: '4'\n For The Volume Of A Sphere Enter: '5'\n For The Area Of A Sphere Enter: '6'\n For Sales Tax Enter: '7'\n For Canadian To AMerican Currency Exchange Enter: '8'\n To Exit Program Enter: '9'\n ")
        
        if x==1:
            volume_of_square()
        elif x==2:
            area_of_square()
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
    
        else:
            print("Invild Command")


pass


def volume_of_square():
    x = int(input("This Is Volume Of Square Enter A Length: "))
    final=x**3
    print("The Volume Is",final)
    return final

def area_of_square():
    x=int(input("This Is Area Of Square, Enter A Side: "))
    ttal=x**2
    print(f"The Area Is {ttal}")
    return ttal

def volume_of_rectangle():
    L = int(input("This Is Volume Of Rectangle, Enter A Length: "))
    W = int(input("Enter A Width: "))
    H = int(input("Enter A Height: "))
    ans = L*W*H
    print(f"The Volume Is {ans}")
    return ans

def area_of_rectangle():
    L = int(input("This Is Area Of Rectangle, Enter A Length: "))
    W = int(input("Enter A Width: "))
    ans = W * L
    print(f"The Area Is {ans}")
    return(ans)

def volume_of_sphere():
    r = int(input("This Is Volume Of Sphere, Enter A Radius: "))
    ans = 4/3 * math.pi * r**3
    print(f"The volume is {ans}")
    return ans

def area_of_sphere():
    r = int(input("This Is Area Of Sphere, Enter A Radius: "))
    area =  4* math.pi *r**2
    print(f"The Area Is {area}")
    return area

def usd_to_cad():
    c=int(input('Enter Amount In USD: '))
    tootal=c*1.37
    print(f"The Total Amount Is {tootal}")
    

def calcTax():
    x=int(input("This Is The Sales Tax Caluclator, Enter Product Price Before Tax: "))
    tax=x*0.12
    total=x+tax
    print(f"Amount Of Taxes {tax} - Total Amount",total)
    return total


menu()


