count_h=0
count_c=0
print("____________________________________Rock___Paper___Scissors____________________________________")
start=input("Are you ready to play if you are ready say Yes:\t ").upper()
if start=="YES":
    keep_playing= True
else:
    print("You dont want to play .....okay then")

while keep_playing:
    import random

    c_choice = random.choice(['rock', 'paper', 'scissors'])
    h_choice = ['rock', 'paper', 'scissors']
    

    def assign_value(list, choice):
     index = list[choice]
     return index
    
    choice=int(input("Your choice:\n 0- Rock\n1- paper\n 2-scissors\n"))
    index = assign_value(h_choice, choice)
    print("Your choice is:\t "+index)
    print("Computer choice was:"+ c_choice)

    if((h_choice=='rock' and c_choice=='scissors') or (h_choice=='scissors' and c_choice=='paper') or(h_choice=='paper' and c_choice=='rock')):
        print("Human wins")
        count_h += 1
    elif(h_choice == c_choice):
         print("draw")
    else :
        print("computer wins")
        count_c += 1

    print("\nDo you want to play again?")
    answer = input().upper()
    if answer == "NO":
        keep_playing = False
        print("\nThanks for playing!")
        print("Computer score is:"+str(count_c))
        print("Human score is :" + str(count_h))

        print("\nOverall results:")
        if count_c > count_h:
            print("Better luck next time!\n")
        elif count_c == count_h:
            print("It is a draw\n")
        else :
            print("You win!\n")
        print("_________________________Rock...Paper...Scissors_________________________")
    
