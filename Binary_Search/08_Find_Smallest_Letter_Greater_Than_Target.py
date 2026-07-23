class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        low = 0
        high = len(letters)-1
        ans = len(letters)

        while low<=high:
            mid = low + (high- low)//2

            if ord (letters[mid])<=ord(target):
                low = mid + 1

            elif ord(letters[mid])>ord(target):
                ans = mid
                high = mid - 1

        if ans == len(letters)  :
            return letters[0]
        return letters[ans]
