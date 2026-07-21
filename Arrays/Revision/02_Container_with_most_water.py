'''
time complexity : O (n)
space complexity: O(1)
'''

def containerwithmostwater(nums):
    left = 0 
    right = len(nums)-1
    max_area=0
    while left<right:
        h = min(nums[left],nums[right])
        width = right - left 
        max_area = max(max_area,h*width)

        if nums[left]>nums[right]:
            right-=1

        else :
            left+=1

    return max_area

