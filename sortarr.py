arr = [6,3,7,9,4,1,2,5]
arrlen = len(arr)
count = 0
n = 0

while count <= arrlen:
    while n <= (arrlen-2):
        if arr[n] > arr[n+1]:
            temp = arr[n]
            arr[n] = arr[n+1]
            arr[n+1] = temp
            print(arr)
        n += 1
    n = 0
    count = 0
