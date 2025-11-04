def leader(nums):
    
    # n=len(nums)
    # ans=[]
    # for i in range(n):
    #     leader=True
    #     for j in range(i+1,n):
            
    #         if nums[j]>nums[i]:
    #             leader=False
    #             break
            
    #     if leader:
    #         ans.append(nums[i])
            
    # return ans
    
    n=len(nums)
    max_element=nums[-1]
    ans=[]
    ans.append(nums[-1])
    
    for i in range(n-2,-1,-1):
        if nums[i]>max_element:
            max_element=max(max_element,nums[i])
            ans.append(nums[i])        
    
    return ans
nums=[10,22,12,3,0,6]
print(leader(nums))