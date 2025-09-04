import random
def validate_num(input_num):
  if not input_num.isdigit():
    print('Invalid input. Please input a number.')
    return False

  input_num= int(input_num)
  if input_num > 100 or input_num < 0:
    print('Invalid number. please enter a number between 0 and 100')
    return False
  return True

def start_game():
  rand_num= random.randint(0, 100)
  score= 100

  while True:
    input_num= input('Guess a number between 0 and 100: ')
    if input_num == 'q':
      print('Goodbye!')
      break

    input_num= int(input_num)
    if input_num == rand_num:
      print(f'Congratulations! You guessed the number {rand_num} in {100 - score} guesses.')
      wanna_play = input('Do you want to play? y/n')
      if wanna_paly == 'y':
        rand_num= random.randint(0 , 100)
        score= 100
        continue
      if wanna_play == 'n':
        print('Goodbye!')
        break

    elif input_num > rand_num:
      print('Your guessed too high!')
    else:
      print('Your guessed too low!')
    score -= 10
    score= max(score, 0)
if __name__=='__main__':
  start_game()
