# Vehicle list
cars = [
    {
      "VehicalNumber": "CAR5581",
      "NoOfSeats": 3,
      "AirCondition": "AC"
    },
    {
      "VehicalNumber": "CAR5661",
      "NoOfSeats": 3,
      "AirCondition": "Non AC"
    },
    {
      "VehicalNumber": "CAR2511",
      "NoOfSeats": 4,
      "AirCondition": "AC"
    },
    {
      "VehicalNumber": "CAR9908",
      "NoOfSeats": 4,
      "AirCondition": "Non AC"
    },
]

vans = [
    {
      "VehicalNumber": "VAN2080",
      "NoOfSeats": 6,
      "AirCondition": "AC"
    },
    {
      "VehicalNumber": "VAN6593",
      "NoOfSeats": 6,
      "AirCondition": "Non AC"
    },
    {
      "VehicalNumber": "VAN8933",
      "NoOfSeats": 7,
      "AirCondition": "AC"
    },
    {
      "VehicalNumber": "VAN4712",
      "NoOfSeats": 8,
      "AirCondition": "AC"
    },
    {
      "VehicalNumber": "VAN8022",
      "NoOfSeats": 8,
      "AirCondition": "Non AC"
    },
]

threeWheelers = [
    {
      "VehicalNumber": "TUK2054",
      "NoOfSeats": 3,
    },
    {
      "VehicalNumber": "TUK3380",
      "NoOfSeats": 3,
    },
    {
      "VehicalNumber": "TUK6895",
      "NoOfSeats": 3,
    },
    {
      "VehicalNumber": "TUK4715",
      "NoOfSeats": 3,
    },
]

trucks = [
    {
      "VehicalNumber": "TRK5361",
      "Size": 12
    },
    {
      "VehicalNumber": "TRk5578",
      "Size": 7
    },
    {
      "VehicalNumber": "TRK1181",
      "Size": 7
    },
    {
      "VehicalNumber": "TRK9801",
      "Size": 12
    },
]

lorries = [
    {
      "VehicalNumber": "LRY5111",
      "Load": 2500
    },
    {
      "VehicalNumber": "LRY7278",
      "Load": 3500
    },
    {
      "VehicalNumber": "LRY1941",
      "Load": 2500
    },
    {
      "VehicalNumber": "LRY9252",
      "Load": 3500
    },
    {
      "VehicalNumber": "LRY1871",
      "Load": 3500
    },
]

# Hired vehicle list
hiredCar = [
    {
      "VehicalNumber": "CAR1465",
      "NoOfSeats": 4,
      "AirCondition": "AC"
    },
    {
      "VehicalNumber": "CAR1906",
      "NoOfSeats": 3,
      "AirCondition": "Non AC"
    },
    {
      "VehicalNumber": "CAR3429",
      "NoOfSeats": 3,
      "AirCondition": "AC"
    },
]

hiredVan = [
    {
      "VehicalNumber": "VAN2381",
      "NoOfSeats": 6,
      "AirCondition": "AC"
    },
    {
      "VehicalNumber": "VAN7460",
      "NoOfSeats": 8,
      "AirCondition": "Non AC"
    },
    {
      "VehicalNumber": "VAN3029",
      "NoOfSeats": 6,
      "AirCondition": "Non AC"
    },
]

hiredTw = [
    {
      "VehicalNumber": "TUK9680",
      "NoOfSeats": 3,
    },
    {
      "VehicalNumber": "TUK3510",
      "NoOfSeats": 3,
    },
    {
      "VehicalNumber": "TUK7620",
      "NoOfSeats": 3,
    },
]

hiredTruck = [
    {
      "VehicalNumber": "TRK7551",
      "Size": 7
    },
    {
      "VehicalNumber": "TRK9961",
      "Size": 12
    },
    {
      "VehicalNumber": "TRK9065",
      "Size": 12
    },
]

hiredLorry = [
    {
      "VehicalNumber": "LRY1495",
      "Load": 3500
    },
    {
      "VehicalNumber": "LRY0171",
      "Load": 2500
    },
    {
      "VehicalNumber": "LRY6502",
      "Load": 2500
    },
]

# Add new vehicle functions

# add car
def addCarFuntion(NoOfSeats,AirCondition,VehicalNumber):
    newDictionary = {
        "VehicalNumber": VehicalNumber,
        "NoOfSeats": NoOfSeats,
        "AirCondition": AirCondition
    }
    cars.append(newDictionary)
    print("\nThe car number ", VehicalNumber," was successfully added to the system.........\n")
    
    print("Car List:")
    for car in cars:
        print("ID: ", cars.index(car) , ", vehical number: ", car['VehicalNumber'],", seats: ", 
        car['NoOfSeats'], ", AC: ", car['AirCondition'])

# add van
def addVanFuntion(NoOfSeats,AirCondition,VehicalNumber):
    newDictionary = {
        "VehicalNumber": VehicalNumber,
        "NoOfSeats": NoOfSeats,
        "AirCondition": AirCondition
    }
    vans.append(newDictionary)
    
    print("\nThe van number ", VehicalNumber," was successfully added to the system.........\n")
    
    print("Van List")
    for van in vans:
        print("ID: ", vans.index(van) , ", vehical number: ", van['VehicalNumber'],", seats: ", 
        van['NoOfSeats'], ", AC: ", van['AirCondition'])
        
# add 3wheeler
def addThreewheelerFuntion(VehicalNumber,NoOfSeats):
    newDictionary = {
        "VehicalNumber": VehicalNumber,
        "NoOfSeats": NoOfSeats
    }
    threeWheelers.append(newDictionary)
    
    print("\nThe threeWheeler number ", VehicalNumber," was successfully added to the system.........\n")
    
    print("ThreeWheelers List:")
    for threeWheeler in threeWheelers:
        print("ID: ", threeWheelers.index(threeWheeler) ,"Vehical number: ", threeWheeler['VehicalNumber'],", seats: ", 
        threeWheeler['NoOfSeats'])

# add truck
def addTruckFuntion(Size,VehicalNumber):
    newDictionary = {
        "VehicalNumber": VehicalNumber,
        "Size": Size
    }
    trucks.append(newDictionary)
    print("\nThe truk number ", VehicalNumber," was successfully added to the system.........\n")
    
    print("Truck List:")
    for truck in trucks:
        print("ID: ", trucks.index(truck) , ", vehical number: ", truck['VehicalNumber'],", Size: ", 
        truck['Size']," ft")

# add lorry
def addLorryFuntion(Load,VehicalNumber):
    newDictionary = {
        "VehicalNumber": VehicalNumber,
        "Load": Load
    }
    lorries.append(newDictionary)
    print("\nThe lorry number ", VehicalNumber," was successfully added to the system.........\n")
    
    print("Lorry List:")
    for lorry in lorries:
        print("ID: ", lorries.index(lorry) , ", vehical number: ", lorry['VehicalNumber'],", Load: ", 
        lorry['Load']," kg")
        
# Remove vehicle functions

# remove car
def removeCarFuntion():
    print("Car List:")
    for car in cars:
        print("ID: ", cars.index(car) , ", vehical number: ", car['VehicalNumber'],", seats: ", 
        car['NoOfSeats'], ", AC: ", car['AirCondition'])
    
    delItem = int(input("\nSelect the ID: "))
    
    print("\nThe car number ", cars[delItem]["VehicalNumber"], " removed from the system...........\n")
    
    cars.pop(delItem)
    
    print("Car List:")
    for car in cars:
        print("ID: ", cars.index(car) , ", vehical number: ", car['VehicalNumber'],", seats: ", 
        car['NoOfSeats'], ", AC: ", car['AirCondition'])

# remove van
def removeVanFuntion():
    print("Van List")
    for van in vans:
        print("ID: ", vans.index(van) , ", vehical number: ", van['VehicalNumber'],", seats: ", 
        van['NoOfSeats'], ", AC: ", van['AirCondition'])
    
    delItem = int(input("\nSelect the ID: "))
    
    print("\nThe van number ", vans[delItem]["VehicalNumber"], " removed from the system...........\n")
    
    vans.pop(delItem)
    
    print("Van List")
    for van in vans:
        print("ID: ", vans.index(van) , ", vehical number: ", van['VehicalNumber'],", seats: ", 
        van['NoOfSeats'], ", AC: ", van['AirCondition'])

# remove 3wheeler
def removeThreeWheelersFuntion():
    print("ThreeWheelers List:")
    for threeWheeler in threeWheelers:
        print("ID: ", threeWheelers.index(threeWheeler) ,"Vehical number: ", threeWheeler['VehicalNumber'],", seats: ", 
        threeWheeler['NoOfSeats'])
    
    delItem = int(input("\nSelect the ID: "))
    
    print("\nThe threeWheeler number ", threeWheelers[delItem]["VehicalNumber"], " removed from the system...........\n")
    
    threeWheelers.pop(delItem)
    
    print("ThreeWheelers List:")
    for threeWheeler in threeWheelers:
        print("ID: ", threeWheelers.index(threeWheeler) ,"Vehical number: ", threeWheeler['VehicalNumber'],", seats: ", 
        threeWheeler['NoOfSeats'])

# remove truck
def removeTruckFuntion():
    print("Truck List:")
    for truck in trucks:
        print("ID: ", trucks.index(truck) , ", vehical number: ", truck['VehicalNumber'],", Size: ", 
        truck['Size']," ft")
    
    delItem = int(input("\nSelect the ID: "))
    
    print("\nThe truck number ", trucks[delItem]["VehicalNumber"], " removed from the system...........\n")
    
    trucks.pop(delItem)
    
    print("Truck List:")
    for truck in trucks:
        print("ID: ", trucks.index(truck) , ", vehical number: ", truck['VehicalNumber'],", Size: ", 
        truck['Size']," ft")

# remove lorry
def removeLorryFuntion():
    print("Lorry List:")
    for lorry in lorries:
        print("ID: ", lorries.index(lorry) , ", vehical number: ", lorry['VehicalNumber'],", Load: ", 
        lorry['Load']," kg")
    
    delItem = int(input("\nSelect the ID: "))
    
    print("\nThe lorry number ", lorries[delItem]["VehicalNumber"], " removed from the system...........\n")
    
    lorries.pop(delItem)
    
    print("Lorry List:")
    for lorry in lorries:
        print("ID: ", lorries.index(lorry) , ", vehical number: ", lorry['VehicalNumber'],", Load: ", 
        lorry['Load']," kg")
        
# hire vehicle functions

# hire car
def hireCarFunction():
    print("Car List:")
    for car in cars:
        print("ID: ", cars.index(car) , ", vehical number: ", car['VehicalNumber'],", seats: ", 
        car['NoOfSeats'], ", AC: ", car['AirCondition'])
        
    CarIndex = int(input("\nSelect the ID: "))
    
    hiredCar.append(cars[CarIndex])
    
    print("\nThe car number ", cars[CarIndex]["VehicalNumber"], " hired...........\n")
    
    cars.pop(CarIndex)
    
    print("Hired List:")
    for hiringCar in hiredCar:
            print("ID: ", hiredCar.index(hiringCar) ,", vehical number: ", hiringCar['VehicalNumber'],", seats: ", 
            hiringCar['NoOfSeats'], ", AC: ", hiringCar['AirCondition'])

# hire van
def hireVanFunction():
    print("Van List")
    for van in vans:
        print("ID: ", vans.index(van) , ", vehical number: ", van['VehicalNumber'],", seats: ", 
        van['NoOfSeats'], ", AC: ", van['AirCondition'])
        
    VanIndex = int(input("\nSelect the ID: "))
    
    
    hiredVan.append(vans[VanIndex])
    print("\nThe van number ", vans[VanIndex]["VehicalNumber"], " hired...........\n")
    vans.pop(VanIndex)
    
    print("Hired List:")
    for hiringVan in hiredVan:
        print("ID: ", hiredVan.index(hiringVan) ,", Vehical number: ", hiringVan['VehicalNumber'],", seats: ", 
        hiringVan['NoOfSeats'], ", AC: ", hiringVan['AirCondition'])

# hire 3wheeler
def hireThreeWheelerFunction():
    print("ThreeWheelers List:")
    for threeWheeler in threeWheelers:
        print("ID: ", threeWheelers.index(threeWheeler) ,"Vehical number: ", threeWheeler['VehicalNumber'],", seats: ", 
        threeWheeler['NoOfSeats'])
        
    threeWheelerIndex = int(input("\nSelect the ID: "))
    
    hiredTw.append(threeWheelers[threeWheelerIndex])
    print("\nThe threeWheeler number ", threeWheelers[threeWheelerIndex]["VehicalNumber"], " hired...........\n")
    threeWheelers.pop(threeWheelerIndex)
    
    print("Hired List:")
    for hiringTw in hiredTw:
        print("ID: ", hiredTw.index(hiringTw) ,", Vehical number: ", hiringTw['VehicalNumber'],", seats: ", 
        hiringTw['NoOfSeats'])

# hire truck
def hireTruckFunction():
    print("Truck List:")
    for truck in trucks:
        print("ID: ", trucks.index(truck) , ", vehical number: ", truck['VehicalNumber'],", Size: ", 
        truck['Size']," ft")
        
    TruckIndex = int(input("\nSelect the ID: "))
    
    hiredTruck.append(trucks[TruckIndex])
    
    print("\nThe truk number ", trucks[TruckIndex]["VehicalNumber"], " hired...........\n")
    
    trucks.pop(TruckIndex)
    
    print("Hired Truck List:")
    for hiringTruck in hiredTruck:
            print("ID: ", hiredTruck.index(hiringTruck) ,", vehical number: ", hiringTruck['VehicalNumber'],", Size: ", 
            hiringTruck['Size']," ft")

# hire lorry
def hireLorryFunction():
    print("Lorry List:")
    for lorry in lorries:
        print("ID: ", lorries.index(lorry) , ", vehical number: ", lorry['VehicalNumber'],", Load: ", 
        lorry['Load']," kg")
        
    LorryIndex = int(input("\nSelect the ID: "))
    
    hiredLorry.append(lorries[LorryIndex])
    
    print("\nThe truk number ", lorries[LorryIndex]["VehicalNumber"], " hired...........\n")
    
    lorries.pop(LorryIndex)
    
    print("Hired Lorry List:")
    for hiringL in hiredLorry:
            print("ID: ", hiredLorry.index(hiringL) ,", vehical number: ", hiringL['VehicalNumber'],", Load: ", 
            hiringL['Load']," kg")

# release vehicle functions

# release Car
def releaseCarFunction():
    print("Hired List:")
    for hiringCar in hiredCar:
            print("ID: ", hiredCar.index(hiringCar) ,", vehical number: ", hiringCar['VehicalNumber'],", seats: ", 
            hiringCar['NoOfSeats'], ", AC: ", hiringCar['AirCondition'])
            
    CarIndex = int(input("\nSelect the ID: "))
    
    print("\nThe car number ", hiredCar[CarIndex]["VehicalNumber"], " released...........\n")
    
    hiredCar.pop(CarIndex)
    cars.append(CarIndex)
    
    print("Hired List:")
    for hiringCar in hiredCar:
            print("ID: ", hiredCar.index(hiringCar) ,", vehical number: ", hiringCar['VehicalNumber'],", seats: ", 
            hiringCar['NoOfSeats'], ", AC: ", hiringCar['AirCondition'])

# release van
def releaseVanFunction():
    print("Hired List:")
    for hiringVan in hiredVan:
        print("ID: ", hiredVan.index(hiringVan) ,", Vehical number: ", hiringVan['VehicalNumber'],", seats: ", 
        hiringVan['NoOfSeats'], ", AC: ", hiringVan['AirCondition'])
    
    VanIndex = int(input("\nSelect the ID: "))
    
    print("\nThe van number ", hiredVan[VanIndex]["VehicalNumber"], " released...........\n")
    
    hiredVan.pop(VanIndex)
    vans.append(VanIndex)
    
    print("Hired List:")
    for hiringVan in hiredVan:
        print("ID: ", hiredVan.index(hiringVan) ,", Vehical number: ", hiringVan['VehicalNumber'],", seats: ", 
        hiringVan['NoOfSeats'], ", AC: ", hiringVan['AirCondition'])

# release 3wheeler
def releaseThreeWheelerFunction():
    print("Hired List:")
    for hiringTw in hiredTw:
        print("ID: ", hiredTw.index(hiringTw) ,", Vehical number: ", hiringTw['VehicalNumber'],", seats: ", 
        hiringTw['NoOfSeats'])
    
    threeWheelerIndex = int(input("\nSelect the ID: "))
    
    print("\nThe threeWheeler number ", hiredTw[threeWheelerIndex]["VehicalNumber"], " released...........\n")
    
    hiredTw.pop(threeWheelerIndex)
    threeWheelers.append(threeWheelerIndex)
    
    print("Hired List:")
    for hiringTw in hiredTw:
        print("ID: ", hiredTw.index(hiringTw) ,", Vehical number: ", hiringTw['VehicalNumber'],", seats: ", 
        hiringTw['NoOfSeats'])

# release Truck
def releaseTruckFunction():
    print("Hired Truck List:")
    for hiringTruck in hiredTruck:
            print("ID: ", hiredTruck.index(hiringTruck) ,", vehical number: ", hiringTruck['VehicalNumber'],", Size: ", 
            hiringTruck['Size']," ft")
            
    TruckIndex = int(input("\nSelect the ID: "))
    
    print("\nThe trucks number ", hiredTruck[TruckIndex]["VehicalNumber"], " released...........\n")
    
    hiredTruck.pop(TruckIndex)
    trucks.append(TruckIndex)
    
    print("Hired Truck List:")
    for hiringTruck in hiredTruck:
            print("ID: ", hiredTruck.index(hiringTruck) ,", vehical number: ", hiringTruck['VehicalNumber'],", Size: ", 
            hiringTruck['Size']," ft")
            
# release Lorry
def releaseLorryFunction():
    print("Hired Lorry List:")
    for hiringL in hiredLorry:
        print("ID: ", hiredLorry.index(hiringL) ,", vehical number: ", hiringL['VehicalNumber'],", Load: ", 
            hiringL['Load']," kg")
            
    LorryIndex = int(input("\nSelect the ID: "))
    
    print("\nThe lorries number ", hiredLorry[LorryIndex]["VehicalNumber"], " released...........\n")
    
    hiredLorry.pop(LorryIndex)
    lorries.append(LorryIndex)
    
    print("Hired Lorry List:")
    for hiringL in hiredLorry:
        print("ID: ", hiredLorry.index(hiringL) ,", vehical number: ", hiringL['VehicalNumber'],", Load: ", 
        hiringL['Load']," kg")

# Available vehical functions

# available car
def availableCars():
    print("\nAvailable Car List:")
    for car in cars:
        print("ID: ", cars.index(car) , ", vehical number: ", car['VehicalNumber'],", seats: ", 
        car['NoOfSeats'], ", AC: ", car['AirCondition'])

#available van 
def availableVans():
    print("\nAvailable Van List")
    for van in vans:
        print("ID: ", vans.index(van) , ", vehical number: ", van['VehicalNumber'],", seats: ", 
        van['NoOfSeats'], ", AC: ", van['AirCondition'])

# available 3wheeler
def availableThreewheels():
    print("\nAvailable ThreeWheelers List:")
    for threeWheeler in threeWheelers:
        print("ID: ", threeWheelers.index(threeWheeler) ,"Vehical number: ", threeWheeler['VehicalNumber'],", seats: ", 
        threeWheeler['NoOfSeats']) 

# available truck
def availableTrucks():
    print("\nAvailable Truck List:")
    for truck in trucks:
        print("ID: ", trucks.index(truck) , ", vehical number: ", truck['VehicalNumber'],", Size: ", 
        truck['Size']," ft")

# available Lorry
def availableLorries():
    print("\nAvailable Lorry List:")
    for lorry in lorries:
        print("ID: ", lorries.index(lorry) , ", vehical number: ", lorry['VehicalNumber'],", Load: ", 
        lorry['Load']," kg")

# User Part
print("Welcome to the Cab Service...\nSelect the number What you want to do..\n")
print("[1]-Add new vehicle\n[2]-Remove vehicle\n[3]-Hire vehicle\n[4]-Release vehicle\n[5]-Check available vehicle\n")
firstInput = int(input("Enter Number:-"))

# add vehicle
if firstInput == 1:
    print("Welcome to add new vehicle...\nEnter number of vehicle type you want to add...\n")
    print("[1]-Car\n[2]-Van\n[3]-Three Wheeler\n[4]-Truck\n[5]-Lorry\n")
    addInput = int(input("Enter Number:-"))
    
    # car
    if addInput == 1:
        VehicalNumber = input("Vehical Number: ")    
        NoOfSeats = int(input("Enter the seat number: "))    
        AirCondition = input("AC or Non-AC: ")
        addCarFuntion(NoOfSeats, AirCondition,VehicalNumber)
    
    # van
    elif addInput == 2:
        VehicalNumber = input("Enter vehical number: ")
        NoOfSeats = int(input("Enter the seat number: "))    
        AirCondition = input("AC or Non-AC: ")
        addVanFuntion(NoOfSeats, AirCondition, VehicalNumber)
    
    # 3wheeler
    elif addInput == 3:
        VehicalNumber = input("Enter vehical number: ")
        NoOfSeats = int(input("Enter the seat number: "))
        addThreewheelerFuntion(VehicalNumber,NoOfSeats)
    
    # truck
    elif addInput == 4:
        VehicalNumber = input("Vehical Number: ")    
        Size = int(input("Enter the size (feet): "))
        addTruckFuntion(Size,VehicalNumber)
    
    # lorry
    elif addInput == 5:
        VehicalNumber = input("Vehical Number: ")    
        Load = int(input("Enter the load (kg): "))
        addLorryFuntion(Load,VehicalNumber)
    
    # error
    else:
        print("Please Enter Valid Number")
        
# delete vehicle
elif firstInput == 2:
    print("Welcome to remove vehicle...\nEnter number of vehicle type you want to remove...\n")
    print("[1]-Car\n[2]-Van\n[3]-Three Wheeler\n[4]-Truck\n[5]-Lorry\n")
    removeInput = int(input("Enter Number:-"))
    
    # car
    if removeInput == 1:
        removeCarFuntion()
    
    # van
    elif removeInput == 2:
        removeVanFuntion()
    
    # 3wheeler
    elif removeInput == 3:
        removeThreeWheelersFuntion()
    
    # truck
    elif removeInput == 4:
        removeTruckFuntion()
    
    # Lorry
    elif removeInput == 5:
        removeLorryFuntion()
    
    # error 
    else:
        print("Please Enter Valid Number")
        
# hire vehicle
elif firstInput == 3:
    print("Welcome to hire vehicle...\nEnter number of vehicle type you want to hire...\n")
    print("[1]-Car\n[2]-Van\n[3]-Three Wheeler\n[4]-Truck\n[5]-Lorry\n")
    hireInput = int(input("Enter Number:-"))
    
    # car
    if hireInput == 1:
        hireCarFunction()
    
    # van
    elif hireInput == 2:
        hireVanFunction()
    
    # 3wheeler
    elif hireInput == 3:
        hireThreeWheelerFunction()
    
    # truck
    elif hireInput == 4:
        hireTruckFunction()
    
    # Lorry
    elif hireInput == 5:
        hireLorryFunction()
    
    # error 
    else:
        print("Please Enter Valid Number")
    
# release vehicle
elif firstInput == 4:
    print("Welcome to release vehicle...\nEnter number of vehicle type you want to release...\n")
    print("[1]-Car\n[2]-Van\n[3]-Three Wheeler\n[4]-Truck\n[5]-Lorry\n")
    releaseInput = int(input("Enter Number:-"))
    
    # car
    if releaseInput == 1:
        releaseCarFunction()
    
    # van
    elif releaseInput == 2:
        releaseVanFunction()
    
    # 3wheeler
    elif releaseInput == 3:
        releaseThreeWheelerFunction()
    
    # truck
    elif releaseInput == 4:
        releaseTruckFunction()
    
    # Lorry
    elif releaseInput == 5:
        removeLorryFuntion()
    
    # error 
    else:
        print("Please Enter Valid Number")
    
# available vehicle
elif firstInput == 5:
    print("Welcome to check available vehicle...\nEnter number of vehicle type you want to release...\n")
    print("[1]-Car\n[2]-Van\n[3]-Three Wheeler\n[4]-Truck\n[5]-Lorry\n")
    avaInput = int(input("Enter Number:-"))
    
    # car
    if avaInput == 1:
        availableCars()
    
    # van
    elif avaInput == 2:
        availableVans()
    
    # 3wheeler
    elif avaInput == 3:
        availableThreewheels()
    
    # truck
    elif avaInput == 4:
        availableTrucks()
    
    # Lorry
    elif avaInput == 5:
        availableLorries()
    
    # error 
    else:
        print("Please Enter Valid Number")
        
# invalid number
else:
    print("Please Enter Valid Number")