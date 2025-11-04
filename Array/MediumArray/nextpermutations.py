from itertools import permutations

def nextpermu(nums):
    
    # all_perm=sorted(permutations(nums))
    
    # current_perm=tuple(nums)
    
    # for i in range(len(all_perm)):
        
    #     if all_perm[i]==current_perm:
            
    #         if i==len(all_perm)-1:
    #             return list(all_perm[0])
            
    #         else:
    #             return list(all_perm[i+1])
            
    # return nums
    
    index=-1
    n=len(nums)
    for i in range(n-2,-1,-1):
        if nums[i+1]>nums[i]:
            index=i
            break
        
    if index==-1:
        rev(0,n-1,nums)
        return nums
    
    for i in range(n-1,index,-1):
        if nums[i]>nums[index]:
            nums[i],nums[index]=nums[index],nums[i]
            break
        
    rev(index+1,n-1,nums)
    
    return nums

def rev(left,right,nums):
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1

nums=[3,2,1]
print(nextpermu(nums))