
def Bubblesort(arr):
    
    n=len(arr)
    for i in range(n-1):
        
        swapped=False
        for j in range(1,n-i):
            
            if arr[j-1]>arr[j]:
                
                arr[j-1],arr[j]=arr[j],arr[j-1]
                swapped=True
                
        
        if not swapped:
            break
        
        
arr=[66,2,44,1,10]
Bubblesort(arr)
print(arr)