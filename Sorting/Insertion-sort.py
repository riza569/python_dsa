def Insertion(arr):
    

    for i in range(len(arr)-1):
        
        j=i+1
        
        while j>0 and arr[j]<arr[j-1]:
            
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1





arr=[66,2,44,1,10]
Insertion(arr)
print(arr)