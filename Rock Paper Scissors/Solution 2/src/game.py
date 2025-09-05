import random


def get_user_choice():
  print("\n1. Rock\n2. Paper\n3. Scissors")
  user_choice= int(input('Enter your choice: '))
  while user_choice not in [1 ,2, 3]:
    user_choice= input('Enter a valid choice: ')
  items= {1: 'rock', 2: 'paper', 3: 'scissors'}
  return items[user_choice]


def get_computer_choice():
  computer_choice= random.randint(1, 3)
  items= {1: 'rock', 2: 'paper', 3: 'scissors'}
  return items[computer_choice]


def determine_winner(user_choice, computer_choice):
  winners= {'paper': 'rock', 'rock': 'scissors', 'scissors': 'paper'}
  if user_choice == computer_choice:
    return(f" Both players selected {user_choice}. It's a tie!")
  if winners[user_choice] == computer_choice:
    return(f"The computer chose {computer_choice}. You win!")
  else:
    return(f"The computer chose {computer_choice}. You lose!")


def play():
  user_choice= get_user_choice()
  computer_choice= get_computer_choice()
  print('user chose: ', user_choice)
  print('computer chose: ', computer_choice)
  print(determine_winner(user_choice, computer_choice))


if __name__ == '__main__':
  play()


