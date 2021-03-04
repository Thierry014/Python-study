

str1 = "Pluto, is a planet."
str2 = str1.split()
a,b,c,d = str1.split()
join_test = '/'.join([a, b, c,d])



# print(f'str1: {str1}, {a},{b},{c},{d}')
# print(f'join_test: {join_test}')
# print(str1)
# print([ word.rstrip(',.') for word in str2])



findstr = ['The Learn Python Challenge Casino.", "They bought a car", "Casinoville']


res = {}
res['one'] = (123)
# print(res)



card = [1,2,3,4,5,6]
card.pop(0)

# print(f'card: {card}')


def calc_hand(hands):
    # hands = [] list 求和
    total = 0
    ace = 0
    for card in hands:
        if card == 'A':
            total += 1
            ace +=1
        elif card in ['J','Q','K']:
            total += 10
        else:
            total += int(card)
            
    return total

# print(calc_hand(['6','K',7]))

word = 'jason'
# print(word.split(' '))   拆分字串


test_list = [1,2,3,4,5,6]
t2 = [1,2,3,2]
dic = {3:1, 4:2, 1:3}
# print(sum(test_list))  list求和
# print(test_list[0:3])
# print(test_list[-3:])

# print(max(test_list))
# test_list.reverse()
# t3 = test_list + t2
# t3.sort()
# print(t3)

list1 = [1,4,5,2,1,7]

start = 1
gap = 2
k = 1
list1 = []
while len(list1) < 11:
    list1.append(start)
    start += gap
    gap += 1

print(list1)