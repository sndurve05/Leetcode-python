class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dict_map={}
        for char in magazine:
            if char in dict_map:
                dict_map[char]+=1
            else:
                dict_map[char]=1

        for char1 in ransomNote:
            if char1 in dict_map:
                dict_map [char1] -=1
            else:
                return False
        
        for val in dict_map.values():
            if val <0:
                return False
        return True