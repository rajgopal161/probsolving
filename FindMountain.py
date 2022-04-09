def findMountain(arr):
    arrlen = len(arr)
    i = 0

    if (i == arrlen-1) or (arrlen < 3):
        print("Invalid Mountain array!!")
        return False

    while (i < (arrlen-2)) and (arr[i] < arr[i+1]):
        i += 1

    while (i <= (arrlen-2)) and (arr[i] > arr[i+1]):
        i += 1

    return i == (arrlen-1)

arr = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
print(findMountain(arr))
