def rotatematrix(nums):
    # n=len(nums)
    
    # dummy=[[0 for _ in range(n)] for _ in range(n)]
    # for i in range(n):
    #     for j in range(n):
            
    #         dummy[j][n-i-1]=nums[i][j]
            
    
    # return dummy

    
    # for i in range(n):
    #     for j in range(i):
            
    #         nums[i][j],nums[j][i]=nums[j][i],nums[i][j]
                 
    # for i in range(n):
    #     nums[i].reverse()
    
        
    # return nums         
    
    n=len(nums)
    m=len(nums[0])
    top=0
    left=0
    right=m-1
    bottom=n-1
    res=[]
    size=n*m
    
    while top<=bottom and left<=right:
        for i in range(left,right+1):
            res.append(nums[top][i])
        top+=1
        
        for i in range(top,bottom+1):
            res.append(nums[i][right])
        right-=1
        
        if  size==len(res):
            break
        
        for i in range(right,left-1,-1):
            res.append(nums[bottom][i])
            
        bottom-=1
        
        for i in range(bottom,top-1,-1):
            res.append(nums[i][left])
            
        left+=1
        
    
    return res
    
arr=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(rotatematrix(arr))
