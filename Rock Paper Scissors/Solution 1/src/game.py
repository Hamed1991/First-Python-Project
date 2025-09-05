import random


class RockPaperScissors:
    def __init__(self, name):
        self.choices = ['rock', 'paper', 'scissors']
        self.name = name

    def get_user_choice(self):
        user_choice = input("Enter your choice (rock, paper, scissors)")
        if user_choice in self.choices:
            return user_choice
        else:
            print("Invalid choice, make sure your choice is in 'rock', 'paper' or 'scissore'")
            return self.get_user_choice

    def get_computer_choice(self):
        return random.choice(self.choices)

    def decide_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return 'It is a tie!'
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
                (user_choice == 'paper' and computer_choice == 'rock') or \
                (user_choice == 'scissors' and computer_choice == 'paper'):
            return f'Congratulations {self.name}. You won!'
        else:
            return 'Oh no! computer won.'

    def play_game(self):
        user_choice = self.get_user_choice()
        computer_choice = self.get_computer_choice()
        print('Computer chose: ', computer_choice)
        print(self.decide_winner(user_choice, computer_choice))


if __name__ == '__main__':
    game = RockPaperScissors('Hamed')
    while True:
        game.play_game()
        continue_game = input("Do you want to play again? (Enter any key to continue or 'q' to quit)")
        if continue_game.lower() == 'q':
            break


