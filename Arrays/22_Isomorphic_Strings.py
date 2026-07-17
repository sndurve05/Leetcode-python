class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map={}
        if len(t)!= len(s):
            return False
        for char,word in zip(t,s):
            if char not in map and word not in map.values():
                map[char]=word
                
            elif char in map and word in map.values():
                  if map[char]!=word:
                        return False

            elif (char in map or word in map.values()) :
                    return False

        return True