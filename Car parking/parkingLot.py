class parkingSpace:
    
    def __init__(self,size):
        self.size = size
        self.slots = [(0,0)] * self.size

    
    def parkCar(self,registrationNo,color ):
        
        availableSlot = self.assign_slot()
        if availableSlot == -1:
            print("Parking space is full !")
            return None
        self.slots[availableSlot] = (registrationNo,color)
        print(f"Please park your Car in slot number : {availableSlot}")

    def exit(self,registrationNo):
        for slot in range(self.size):
            if self.slots[slot][0] == registrationNo:
                self.slots[slot] = (0,0)
                return slot

    def assign_slot(self):
        for slot in range(self.size):
            if self.slots[slot] == (0,0):
                return slot
        else:
            return -1

    def slotOfCarByRegNo (self,registrationNo):
        
        for slot in range(self.size):
            if self.slots[slot][0] == registrationNo:
                print(f"The Car with Registration number '{registrationNo}' is parked in slot no. {slot}")
                break
        else:
            print("There is no such car parked here")

    def slotsOfCarsByColor (self,color):
        sameColoredCars = []
         
        for i in range(self.size):
            if self.slots[i][1] == color:
                sameColoredCars.append(i)

        print(f"The cars with color {color} is present is following slots: {sameColoredCars}")
