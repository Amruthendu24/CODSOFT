import random
def get_computer_choice():
    return random.choice(['rock','paper','scissors'])

def determine_winner(user_choice,computer_choice):
    if user_choice==computer_choice:
        return 'tie'
    elif(user_choice=='rock'and computer_choice=='scissors') or \
        (user_choice=='scissors' and computer_choice=='paper') or \
            (user_choice=='paper' and computer_choice=='rock'):
        return 'user'
    else:
        return 'computer'
    
def display_result(user_choice,computer_choice,winner):
    print(f"\nYou chose:{user_choice}")
    print(f"Computer chose:{computer_choice}")
    
    if winner=='tie':
        print("it's a tie")
    elif winner=='user':
        print("You win!")
    else:
        print("You lose!")
        
def play_game():
    user_score = 0
    computer_score = 0
    play_again = 'yes'
    
    while play_again.lower() == 'yes':
        user_choice=input("choose rock,paper,or scissors:").lower()
        while user_choice not in['rock','paper','scissors']:
            user_choice=input("invalid choice.please choose rock,paper or scissors:").lower()
        computer_choice=get_computer_choice()
        winner=determine_winner(user_choice,computer_choice)   
        
        if winner == 'user':
            user_score+=1
        elif winner=='computer':
            computer_score+=1
            
        display_result(user_choice,computer_choice,winner) 
        
        print(f"\nScore:You{user_score}-{computer_score},computer")
        
        play_again=input("Do you want to play again?(yes/no):").lower()
        while play_again not in['yes','no']:
            play_again=input("Invalid input.Do you want to play again?(yes/no: ").lower()
             
    print("\nThanks for Playing!")
play_game()
                             
              
              
        
 
        