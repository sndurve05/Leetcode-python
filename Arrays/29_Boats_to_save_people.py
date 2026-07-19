class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        left, right = 0 , len(people)-1
        boat = 0 
        while left<=right:
            if people[left] + people[right] <= limit:
                boat+=1
                left+=1
                right-=1
            else:
                if people[left]==limit:
                    boat = len(people)
                boat+=1
                right-=1
                       
        return boat