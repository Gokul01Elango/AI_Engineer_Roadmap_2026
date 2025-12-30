"""
Given an array of integers nums, return the second-largest element in the array. 
If the second-largest element does not exist, return -1.

# give input of arrays

 array= [ -12121, 5 , 8 , 9 ,12121234 ]



"""



def second_largest(arr):
    max=arr[0]
    smax=arr[0]
    for i in arr:
        if max < i :
            smax=max
            max = i
            
            # print(max)
            # print(smax)
        elif max>i and i>smax:
            smax=i
    print(max)
    print(smax)

arr=[  -12121, 5 , 8 , 9 ,12121234  ]

second_largest(arr)


