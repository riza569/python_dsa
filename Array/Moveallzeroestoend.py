def moveallzeroes(arr):
    i=0
    for j in range(len(arr)):
        
        if arr[j]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
    
    
    
nums=[1,2]
moveallzeroes(nums)
print(nums)

    # res=[]
    # cnt=0
    # for i in nums:
    #     if i!=0:
    #        res.append(i)
    #     else:
    #         cnt+=1
            
    # for i in range(cnt):
    #     res.append(0)
    
    # return res
    