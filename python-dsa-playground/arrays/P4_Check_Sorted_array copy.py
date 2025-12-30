"""
Given an array nums of n integers, return true if the array nums is sorted in non-decreasing order or else false.

Example 1

Input : nums = [1, 2, 3, 4, 5]

Output : true


"""

def sorted_array(arr):

    for a,b in zip (arr,arr[:-1]):
        print(b)
    #     if a<b :
    #         # print(i)
    #         return False
            
    
    # return True
            

arr=[12,1,2,3,4,5,2,4]

print(sorted_array(arr))