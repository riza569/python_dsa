def missing(arr,n):
    # for j in range(1,len(arr)):
    #     if arr[j]!=arr[j-1]+1:
    #         return arr[j-1]+1
        
    # hashs={}
    # for number in arr:
    #     hashs[number]=hashs.get(number,0)+1
    
    
    # n=len(arr)
    # for i in range(1,n+1):
    #     if i not in hashs:
    #         return i
           
    # return -1
        
        
    # sum=  (n*(n+1))//2
    # arr_sum=0
    # for num in arr:
    #     arr_sum+=num

    # return sum-arr_sum
    missing=n
    for i,num in enumerate(arr):
        missing^=i
        missing^=num
        
    print(f"{missing}")

        
        
arr=[0,1,2,4,5]
missing(arr,len(arr))