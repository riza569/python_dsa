# def setrow(n,m,i,nums):
#     for j in range(m):
#         if nums[i][j]!=0:
#             nums[i][j]=-1
            
# def setcol(n,m,j,nums):
#     for i in range(n):
#         if nums[i][j]!=0:
#             nums[i][j]=-1

def matrixzero(nums):
    
    # n=len(nums)
    # m=len(nums[0])
    
    # for i in range(n):
    #     for j in range(m):
    #         if nums[i][j]==0:
    #             setrow(n,m,i,nums)
    #             setcol(n,m,j,nums)
                
    # for i in range(n):
    #     for j in range(m):
    #         if nums[i][j]==-1:
    #             nums[i][j]=0
    
    # n=len(nums)
    # m=len(nums[0])
    # row=[0]*n
    # col=[0]*m
    # for i in range(n):
    #     for j in range(m):
    #         if nums[i][j]==0:
    #             row[i]=1
    #             col[j]=1
                
    # for i in range(n):
    #     for j in range(m):
    #         if row[i]==1 or col[j]==1:
    #             nums[i][j]=0
    
    
    n=len(nums)
    m=len(nums[0])
    rowzero=False
    
    for i in range(n):
        for j in range(m):
            if nums[i][j]==0:
                nums[0][j]=0
                if i>0:
                    nums[i][0]=0
                else:
                    rowzero=True
    
    for i in range(1,n):
        for j in range(1,m):
            if nums[0][j]==0 or nums[i][0]==0:
                nums[i][j]=0
    
    
    if nums[0][0]==0:
        for i in range(n):
            nums[i][0]=0
            
    if rowzero==True:
        for j in range(m):
            nums[0][j]=0
        
    
                     
arr=[[1,0,2,0],[3,4,5,2],[1,3,1,5]]
matrixzero(arr)
print(arr)