
def trainSeating():

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


    print("\nMainBerth------------| SideBerth------------| \n")

    while count < itr:
        for i in range(n, seat[count]):
            if i <= (n + 2):
                mainOppComp.append(i)
            elif i <= (n + 5):
                maincomp.append(i)
            else:
                sidecomp.append(i)
        count += 1
        n += 8

        print(str(mainOppComp[0]) + "(LB)", str(mainOppComp[1]) + "(MB)", str(mainOppComp[2]) + "(UB)", " : ", str(sidecomp[0]) + "(LB)", str(sidecomp[1]) + "(UB)")
        print(str(maincomp[0]) + "(LB)", str(maincomp[1]) + "(MB)", str(maincomp[2]) + "(UB)")
        print("---------------------------------------|")

        maincomp = []
        sidecomp = []
        mainOppComp = []

    print("--------------------------------------------------------")
    print("LB : LowerBerth | MB : MiddleBerth | UB : UpperBerth")
    print("--------------------------------------------------------")

trainSeat = int(input("Please enter the seat number : "))
trainCap = 73

if trainSeat >= trainCap:
    print("Your train seat is invalid")
else:
    trainSeating()

