arr = [1,3,0,5,0,7,0,8]
#arr = str(arr)
finarr = []
zarr = []

for i in arr:
    if i != 0:
        finarr.append(i)
    else:
        zarr.append(i)
        
#for i in arr:
#    if i == 0:
#        finarr.append(i)
#        print(i)
        
#print(finarr)

resarr = []
resarr = finarr + zarr
        
print(resarr)


        
    
