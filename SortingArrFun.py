def sortarr(arr):
    arrlen = len(arr)
    count = 0
    n = 0
    while count <= arrlen-3:
        while n <= (arrlen-2):
            if arr[n] > arr[n+1]:
                temp = arr[n]
                arr[n] = arr[n+1]
                arr[n+1] = temp
                
            
            n += 1
        if count == (arrlen-3):
            return(arr)
        n = 0
        count += 1
        
        
    
arr = [6,3,7,9,4,8,1,2,5]
print(arr, "Before Sorting")
print(sortarr(arr), "After Sorting")
