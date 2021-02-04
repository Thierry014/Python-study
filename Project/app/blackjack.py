
import random 

game = 'blackjack'
hands_player = []
hands_dealer = []
card_deck = []

# bet = int(input('How much u want to bet? ')) 



def ini_cards():
    for i in range(3,11):
        card_deck.extend([i]*4)
    
    for j in ['J','Q','K','A']:
        card_deck.extend([j]*4)
    return card_deck





def playgame ():
    is_over = False
    ini_cards()
    random.shuffle(card_deck)
    print(card_deck)

    #发牌
    def fapai(who):
        def remove_first_card():
            card_deck.pop(0)

        if who == 'player':
            hands_player.append(card_deck[0])
            remove_first_card()
            print(f'player-hands is: {hands_player}')
        else:
            hands_dealer.append(card_deck[0])
            remove_first_card()
            print(f'dealer-hands is: {hands_dealer}')

    
    fapai('player')
    fapai('dealer')
    fapai('player')


    print(f'player: {hands_player}, dealer: {hands_dealer}')


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

            if total <= 11 and ace >=1:
                total += 10
       return total
        
    
    keep_fapai = input('Keep going? Y or N ')
    while keep_fapai != 'n':
        fapai('player')
        if calc_hand(hands_player) > 21:
            print('player busted, u lost TOT')
            # todo 
            # calculate rewards
            is_over = True
            break
        keep_fapai = input('Keep going? Y or N ')


    if not is_over:
       while calc_hand(hands_dealer) < 16:
            fapai('dealer')
            if calc_hand(hands_dealer) > 21:
               print('deal busted, u win !o!')
               is_over = True
               break
    
       print(f'player: {hands_player} = {calc_hand(hands_player)}')
       print(f'deal: {hands_dealer} = {calc_hand(hands_dealer)}')

    if not is_over:
       if calc_hand(hands_player) >= calc_hand(hands_dealer) and calc_hand(hands_dealer < 21):
                print('you win')
           # cal reward
       else:
               print('you lose')










playgame()