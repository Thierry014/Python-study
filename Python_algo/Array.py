 #! Array in Python are: List[], tuple(), and string
 #? All support using index  

#  use index describe the location => reference variable 
#  64 bytes => empty list


# todo Q1 check 2 array made up of same letters (anagram).

def check_anagram(l1,l2):
    # remove space
    l1 = l1.replace(' ','').lower()
    l2 = l2.replace(' ','').lower()
    # sort list 
    # check same ==
    return True if sorted(l1) == sorted(l2) else False
 
 # print(check_anagram('do2g','god')) 


# todo lst = [1,3,2,2] => return sum to k (k=4 return [(1,3),(2,2)]) 

def sumToK(lst,k):
    res = []
    # start from next find remain 
    for i,num in enumerate(lst):
        if k-num in lst[i+1:]:
            res.append((num,k-num))
    
    return res

# print(sumToK([1,3,2,2],4))

#todo Maxium of sum 
def sumMax(lst):
    # [1,2,3,-1,2,5,6,7,8,-2]
    temp = 0 
    max_res = 0 

    for i, num in enumerate(lst):
        if temp >= 0:
            temp += num
            max_res = max(temp,max_res)
        else:
            temp = 0 
    return max_res

# print(sumMax([7,1,2,-1,3,4,10,-12,3,21,-19]))

# todo rotate means index sequence 

def rotation(l1,l2):
    dic = {}
    dic[l1[-1]] = l1[0]

    for i in range(len(l1)-1):
        dic[l1[i]] = l1[i+1]
    
    for j in range(len(l2)-1):
        # check last 
        try:
            if dic[l2[-1]] != l2[0]:
                return False
        except KeyError:
            return False

        if dic[l2[j]] != l2[j+1]:
            return False
    return True
            

# print(rotation([6,7,8,1,2,3],[1,2,3,6,7,8]))



#  todo common elements (in same position )
def find_common(l1,l2):
    a = 0
    leng = min(len(l1),len(l2))
    res = []

    print(leng)

    while leng>0:
        if l1[a] == l2[a]:
            res.append(l1[a])
        
        a += 1
        leng -= 1
    
    return res

# print(find_common([1,3,4,6,7,9],[1,2,4,5,9,10]))

def find_common_ele(l1,l2):
    comm = []
    long = l1
    short = l2
    if len(l1) < len(l2):
        long = l2
        short = l1
    
    for num in short:
        if num in long:
            comm.append(num)
        
    return comm

# print(find_common_ele([1,3,4,6,7,9],[1,2,4,5,9,10]))

# todo two pointer solve find common elements 

def two_pointer(l1,l2):
    p1,p2 = 0,0
    res = []

    while p1<len(l1) and p2<len(l2):
        if l1[p1] == l2[p2]:
            res.append(l1[p1])
            p1 += 1
            p2 += 1

        elif l1[p1] > l2[p2]:
            p2 += 1
        else:
            p1 += 1
    
    return res

# print(two_pointer([1,3,4,6,7,9],[1,2,4,5,9,10]))

# todo most frequent elements 
def most_appear(lst):
    dic = {}
    for num in lst: 
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1
    
    return sorted(dic, key= lambda k: dic[k], reverse= True)[0]

print(most_appear([1,3,2,3,4,5,12,1,4,12,4,5,2,2]))



