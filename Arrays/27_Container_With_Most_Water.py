class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left =0 
        right = len(height)-1
        while left<right:
            h = min(height[left],height[right])
            width = right - left
            max_area = max(max_area, (h * width))
            if height[left]>height[right] :
                right -=1
            else:
                left +=1

        return max_area