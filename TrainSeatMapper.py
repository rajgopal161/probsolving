def trainSeating(trainSeat):
    trainSeat = str(trainSeat)
    seat = []
    train = list(range(1, trainCap))
    # print("The Size of train : \n",train)
    for i in train:
        if i % 8 == 0:
            seat.append(i + 1)
    # print("\nSeating Capacity in each compartment : \n",seat)
    itr = len(seat)
    count = 0
    maincomp = []
    sidecomp = []
    mainOppComp = []
    n = 1


    print("--------------------------------------------------------------------------------------------------------")
    print("LB : LowerBerth | MB : MiddleBerth | UB : UpperBerth | SLB : SideLowerBerth | SUB : SideUpperBerth |")
    print("--------------------------------------------------------------------------------------------------------")
    
    while count < itr:
        for i in range(n, seat[count]):
            if i <= (n + 2):
                mainOppComp.append(i)
            elif (i >= (n + 3)) and (i <= (n + 5)):
                maincomp.append(i)
            else:
                sidecomp.append(i)
        
        count += 1
        n += 8
        
        if (trainSeat in (str(mainOppComp[0])) or (trainSeat in str(maincomp[0])) or (trainSeat in str(sidecomp))):
            if (trainSeat in str(sidecomp[0])):
                print(trainSeat + "(SLB)")
                return trainSeat
            print(trainSeat + "(LB)")
            return trainSeat
        elif (trainSeat in (str(mainOppComp[1])) or (trainSeat in str(maincomp[1]))):
            print(trainSeat + "(MB)")
            return trainSeat
        elif (trainSeat in (str(mainOppComp[2])) or (trainSeat in str(maincomp[2])) or (trainSeat in str(sidecomp))):
            if (trainSeat in str(sidecomp[1])):
                print(trainSeat + "(SUB)")
                return trainSeat
            print(trainSeat + "(UB)")
            return trainSeat
        
        maincomp = []
        sidecomp = []
        mainOppComp = []

trainSeat = int(input("Please enter the seat number : "))
trainCap = 73

if trainSeat >= trainCap:
    print("Your train seat is invalid")
else:
    trainSeating(trainSeat)
