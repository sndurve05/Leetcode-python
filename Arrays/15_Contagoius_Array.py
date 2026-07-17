class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix_index = {0:-1}   #creating hash map by storing initial sum as 0 and index -1
        current_sum = 0
        max_len = 0

        for i in range(len(nums)):
            num = nums[i]
            if num == 1:
                current_sum += 1           #if 1 is present add 1 in sum
            else:
                current_sum -= 1          # if 0 is present add -1 in sum

            if current_sum in prefix_index:    #if current_sum is already in prefix_index..it means that the sum of elements between them is 0 i.e. eqaual number of 1s and 0s as 0 is treated as -1 for sum
                sub = i - prefix_index[current_sum]
                max_len = max(max_len,sub)
            else:
                prefix_index[current_sum]=i

        return max_len