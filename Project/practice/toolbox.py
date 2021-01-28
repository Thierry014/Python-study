def find_max():
    # list1 = list(input('Enter List: '))
   
    
    list1 = [1,2,6,232,12,99]
    max_num = list1[0]

    for x in list1:
        if x > max_num:
            max_num = x

    print(max_num)
    return max_num


