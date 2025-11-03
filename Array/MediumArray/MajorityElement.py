def majelement(nums):
   
    # for i in range(len(arr)):
    #     cnt=0
    #     for j in range(i,len(arr)):
    #         if arr[j]==arr[i]:
    #             cnt+=1
                
    #             if cnt>len(arr)//2:
    #                 return arr[j]   
    # n=len(arr)
    # hashmap={}
    # for num in nums :
    #     hashmap[num]=hashmap.get(num,0)+1
        
    # for key,value in hashmap.items():
    #     if value>n//2:
    #         return key
            
    n=len(nums)
    cnt=0
    ele=None
    for i in range(n):
        if cnt==0:
            cnt=1
            ele=nums[i]
        elif arr[i]==ele:
            cnt+=1
        else:
            cnt-=1
    
    cnt1=0
    for i in nums:
      if i==ele:
          cnt1+=1
          
    if cnt1>n//2:
        return ele
    return -1  
arr=[3,2,3]
print(majelement(arr))
