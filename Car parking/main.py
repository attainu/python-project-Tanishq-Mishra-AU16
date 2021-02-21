import time
from menu import *
#from parkingL1ot import *
import parkingLot as parkingLot

if __name__ == "__main__":
    menu1()
    inputOption = input()
    if inputOption == "1" :
        size = int(input("What is the size of your parking Space? "))
        parking_place = parkingLot.parkingSpace(size)  
        
        menu2()
        while True:
            
            Options = input()

            if Options == "1":
                regNo = input("Please Enter the registration number: ")
                color = input("What is the color of your car? ")
                parking_place.parkCar(regNo,color)
            

            elif Options == "2":
                regNo = input("Please Enter the registration number: ")
                
                print(f"Your car with regNo - {regNo} is exited from slot no. {parking_place.exit(regNo)}")

            elif Options == "3":
                regNo = input("Please Enter the registration number of your car: ")
                parking_place.slotOfCarByRegNo(regNo)

        
            elif Options == "4":
                color = input("Please type the color of the car: ").lower()
                parking_place.slotsOfCarsByColor(color)

            elif Options.lower() == "quit" or Options.lower() == "exit":
                break

            else:
                print("Please select a valid option")