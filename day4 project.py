rock= '''
                                         _____
        \                              /\| | | |
         \                            / /|_|_|_|
          \                           \        |
            (  ( ) ) ( )  )            \_______/
           ( ( ( ( )  )  ) )           /______/
          ( ( )) ) (   ) ( ( )        /       /
          ( (__.-.___.-.__) )        /       /
           /---._.---._.---\        /       /
           \||   '/  '   ||/       /       /
            |||  (_     |||       /       /
             || ///\\\  ||\______/       /
        ___/ ||||\__/|||||/             /
       /   \   ||||||||  /             /
      /     \   ||||||  /        _____/
'''
scissiors= '''
 ____
  / __ \
 ( (__) |___ ___
  \________,'   """""----....____
   _______<  () dd       ____----'
  / __   __`.___-----""""
 ( (__) |
  \____/
'''
paper='''
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'
'''
game_images=[rock,scissiors,paper]

user_choice=int(input("What do you choose? type 0 for rock, 1 for paper or 2 for scissors.\n"))
print("user_choose: ")
print(game_images[user_choice])
computer_choice=random.randint(0,2)
print('Computer choose:')
print(game_images[computer_choice])
#logic rock beat scissors means 0 beats 2, 2 beats 1 and 1 beats 0
if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice >=3 or user_choice < 0 :
    print("You type invaild number")
elif computer_choice ==0 and user_choice==2 :
    print("You lose")
elif user_choice > computer_choice:
    print("You win")
elif computer_choice > user_choice:
    print("You lose")
elif computer_choice == user_choice:
    print("It's draw")