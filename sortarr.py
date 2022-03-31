arr = [6,10,3,7,9,4,8,1,2,5]
arrlen = len(arr)
count = 1
n = 0

while count <= (arrlen-3):
    while n <= (arrlen-2):
        if arr[n] > arr[n+1]:
            temp = arr[n]
            arr[n] = arr[n+1]
            arr[n+1] = temp
            
        n += 1
        
    n = 0
    count += 1
    print(arr)
