def restoreIpAddresses( s):
        
    output=[]
    def backtrack(path,start=0,dot=0):

        if dot>4:
            return 
        if dot==4 and start==len(s):
            output.append(path)
            return
        
        if dot <3:
            for i in range(start+1,start+4):

                if i > len(s):
                    break
                 
                num = s[start:i]

                if (len(num)>1 and num[0]=="0"):
                    break

                if (int(num)>255):
                    break
                
                backtrack(path +num+".",i,dot+1)
                

        elif dot==3 :
            if start==(len(s)):
                return
            num = s[start:]

            if (len(num)>1 and num[0]=="0") :
                return
            
            if (int(num)>255) or len(num)>3:
                return
            backtrack(path+num,len(s),dot+1)

    backtrack("")
    return output

print(restoreIpAddresses("101023"))