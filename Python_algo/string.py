 # todo reverse string 

 #! reverse each letter

def rev(str):
     return str[::-1]

# print(rev('God like a great joe'))

#! reverse by words 

def ver_words(str):
    str = str.split(' ')[::-1]
    return (' ').join(str)

# print(ver_words('God like a great joe'))


# todo find unique or not 

def unique(str):
    dic = {}
    str.replace(' ','').lower()

    for char in str:
        if char in dic:
            return False
        else:
            dic[char] = 0
        
    return True


print(unique('abcb'))