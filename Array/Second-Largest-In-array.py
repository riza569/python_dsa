def Largest(arr):
    max=0
    second_max=0
    for i in arr:
        if i>max:
            second_max=max
            max=i

        elif i>second_max and i!=max:
            
            second_max=i
          
    print(f"max:{max} - second max {second_max}")
          
arr=[2,5,1,3,30]
Largest(arr)