def trainSeating(trainSeat):
    
    seat = []
    train = list(range(1, trainCap))
    # print("The Size of train : \n",train)
    for i in train:
        if i % 8 == 0:
            seat.append(i + 1)
    # print("\nSeating Capacity in each compartment : \n",seat)
    itr = len(seat)
    count = 0


    print("--------------------------------------------------------------------------------------------------------")
    print("LB : LowerBerth | MB : MiddleBerth | UB : UpperBerth | SLB : SideLowerBerth | SUB : SideUpperBerth |")
    print("--------------------------------------------------------------------------------------------------------")
    
    while count < itr:
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
            
            count += 1
        

trainSeat = int(input("Please enter the seat number : "))
trainCap = 73

if trainSeat >= trainCap:
    print("Your train seat is invalid")
else:
    trainSeating(trainSeat)
