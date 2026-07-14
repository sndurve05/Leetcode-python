def restoreIpAddresses( s):
        
    output=[]
    def backtrack(num,path,start=0,dot=0):
        if dot>3:
            return 
        if dot==3 and len(path)==len(s)+3:
            output.append(path)
            return
            
        for j in range(start,len(s)):

            for i in range(start+1,len(s)+1):
                num = s[start:j]
                if (len(num)>1 and num[0]=="0") or (int(num)>255):
                    continue

                path = num + "."
                backtrack("",path,j,dot+1)
                
      
    return output