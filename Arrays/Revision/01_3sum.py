#20/07/26
'''
Time Complexity:  O(n²)

Space Complexity:  O(1) extra (excluding the output list)
'''

def threesum(nums):

    nums.sort()
    output=[]

    for i in range(len(nums)-2):
        if i > 0 and nums[i]==nums[i-1]:
            continue

        if nums[i] > 0:
            break

        num1 = nums[i]
        left = i+1
        right = len(nums)-1
        target = -1*num1
        while left<right:
            while left>i+1 and left<right and nums[left]==nums[left-1]:
                left+=1
                continue
            while right<len(nums)-1 and left<right and nums[right]==nums[right+1]:
                right-=1
                continue

            if nums[left]+nums[right] == target:
                output.append([num1, nums[left], nums[right]])
                left+=1
                right-=1
            
            elif nums[left]+nums[right]>target:
                right-=1

            elif nums[left]+nums[right]<target:
                left+=1

    return output


print(threesum([-1,0,1,2,-1,-4]))