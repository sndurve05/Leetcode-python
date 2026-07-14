def string(s):
    output=[]
    def backtrack(start,sub,path):
        if len("".join(path))==len(s):
            output.append(path[:])
            return
        
        def palindrome(string,index=0):
            if index>(len(string)//2) or len(string)==0:
                return True
            if string[index]==string[len(string)-index-1]:
                return palindrome(string,index+1)                
            return False

        for i in range(start,len(s)):
            for j in range (i+1,len(s)+1):

                sub = s[i:j]

                if not palindrome(sub):
                    sub=""
                    continue
                path.append(sub)

                backtrack(j,"",path)
                path.pop()
    backtrack(0,"",[])
    return output

print(string("aab"))