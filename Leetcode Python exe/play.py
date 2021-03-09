def strToNum(s):
    dic = {}
    res = ''
    for i in range(1,len(s)+1):
        dic[s[i-1]] = i 
    
    print(dic)
    for i in s:
        res += str(dic[i])
            
    return res

print(strToNum('add'))