#!python3
# Volume Calculator
# Feel free to rename your variables

import math
def menu():
    print("For The Volume Of A Square Enter: '1'\n For The Area Of A Square Enter: '2'\n For The Volume Of A Rectangle Enter: '3'\n For The Area Of A Rectangle Enter: '4'\n For The Volume Of A Sphere Enter: '5'\n For The Area Of A Sphere Enter: '6'\n For Sales Tax Enter: '7'\n For Canadian To AMerican Currency Exchange Enter: '8'")
    input()
    if input=="1":
     if input=="2":
      if input=="3":
       if input=="4":
        if input=="5":
         if input=="6":
          if input=="7":
            calcTax
if input=="8":
               


    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: Copper
    # Modified:
    # title
 pass

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:
    return None



def main():
    """
    main block of code that will run your program and control program flow
    You will need to include a while loop to keep repeating the commands until
    the user chooses to exit
    """

    while True:
        # keep giving options to choose menu options until they choose to exit
        pass

if __name__ == "__main__":
    main()

pass
def calcTax():
 x=input("Enter Product Price Before Tax")
 tax=x*0.12
 total=x+tax
 print("Amount Of Taxes{tax}. Total Amount",total)
pass