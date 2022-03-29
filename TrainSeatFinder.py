def trainSeating(trainSeat):
    
    print("--------------------------------------------------------------------------------------------------------")
    print("LB : LowerBerth | MB : MiddleBerth | UB : UpperBerth | SLB : SideLowerBerth | SUB : SideUpperBerth |")
    print("--------------------------------------------------------------------------------------------------------")
    
    if (trainSeat % 8 == 4) or (trainSeat % 8 == 1):
        print(str(trainSeat) + "(LB)")
        return trainSeat
    elif (trainSeat % 8 == 5) or (trainSeat % 8 == 2):
        print(str(trainSeat) + "(MB)")
        return trainSeat
    elif (trainSeat % 8 == 6) or (trainSeat % 8 == 3):
        print(str(trainSeat) + "(UB)")
        return trainSeat
    elif trainSeat % 8 == 7:
        print(str(trainSeat) + "(SLB)")
        return trainSeat
    elif trainSeat % 8 == 0:
        print(str(trainSeat) + "(SUB)")
        return trainSeat
            
        

trainSeat = int(input("Please enter the seat number : "))
trainCap = 73

if trainSeat >= trainCap:
    print("Your train seat is invalid")
else:
    trainSeating(trainSeat)
