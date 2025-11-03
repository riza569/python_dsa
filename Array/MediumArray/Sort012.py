def sortarray(arr):
    i=0
    for j in range(len(arr)):
        if j ==0:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            
    
arr=[0,2,2,1,1,0]
sortarray(arr)
print(arr)