
def findGCD( nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        max_divisor=1
        num1= nums[0]
        num2= nums[-1]

        for i in range(1, num1 + 1):
    
            if num1%i==0 and num2%i==0:
                
                max_divisor= max(max_divisor, i)
                
        return max_divisor

print(findGCD([2,5,6,9,10]))