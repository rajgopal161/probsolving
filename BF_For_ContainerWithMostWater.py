arr = [10, 1, 4, 5, 3, 8, 2]
area = 0
arrlen = len(arr)
for i in range(0,arrlen-1):
    for j in range(0,arrlen-1):
        narea = (min(arr[i], arr[j+1])) * ((j+1) - i)
        area = max(narea,area)
        #print(arr[i], arr[j+1], (j+1), i)
print(area)
