

str1 = "Pluto, is a planet."
str2 = str1.split()
a,b,c,d = str1.split()
join_test = '/'.join([a, b, c,d])



# print(f'str1: {str1}, {a},{b},{c},{d}')
# print(f'join_test: {join_test}')
print(str1)
print([ word.rstrip(',.') for word in str2])



findstr = ['The Learn Python Challenge Casino.", "They bought a car", "Casinoville']


res = {}
res['one'] = (123)
print(res)



card = [1,2,3,4,5,6]
card.pop(0)

print(f'card: {card}')


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
print(word.split(' '))