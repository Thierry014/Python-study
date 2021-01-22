
# while loop
# i = 1
# while i<5 :
#     print(i)
#     i =i+1
# print('done')


# ***guess number game 

# target = 9
# count = 0

# while count <3 :
#     user_input = int(input('guess a num! '))
#     count = count + 1

#     if int(user_input) == target:
#         print('Yes')
#         break
#     else:
#         print('No')
#         if count == 3 :
#             print('game over')

# ***car game

command = input('tell me what to do! ')
started = False

while command != 'quit':
    if command == 'start':
        print('car start')
        
    elif command == 'stop':
        print('car stopped')
    else:
        print("I don't understand")
    command = input('tell me what to do! ')

    # to do manage the state of the car 
    
