import random


def play_game():
    choices=["Rock","Paper","Scissors"]
  
    
  
    print("==========Welcome To Rock_Paper_Scissors Game==========\n ")
    print("Winning Rule :")
    print("Paper vs Scissors -> Scissors win")
    print("Rock vs Paper -> Paper win")
    print("Rock vs Scissors -> Rock win\n")

    while True:
    
        print("Choose an option :")
        print("1 - Rock")
        print("2 - Paper")
        print("3 - Scissors")
    
        player_input=input("Enter your choice(1-3):")
        if player_input.isdigit():
            choice=int(player_input)
            if 1<= choice <=3:
                print("Correct and continue")
            else:
                print("Please enter number 1-3")
        else:
            print("Pleasse enter number only:")
           
        player_choice = choices[choice - 1]
        print("Player choice is:",player_choice)
    
           
        comp_choice = random.randint(1,3)
        computer_choice = choices[comp_choice - 1]
        print("Computer choice is:",computer_choice)

        if player_choice==computer_choice:
            print("It's a tie!\n")
    
        elif (player_choice==1 and computer_choice==3) or (player_choice==2 and computer_choice==1) or (player_choice==3 and computer_choice
                                                                                                ==2):
            print("You win this round!\n")
       
    
        else:
            print("Computer wins this round!\n")
       
        ans = input("Do you want to play again?(Y/N):")
        if ans.upper()=='N':
            print("Thank you for playing game.")
            break
    
if __name__ == "__main__":
      play_game()
    
    

    