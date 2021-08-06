import random
from art import logo

numbers = []
for number in range(1, 101):
  numbers.append(number)

number_chosen_by_computer = random.choice(numbers)

print(logo)
print("Welcome to Number Guesser game!")
print("I am thinking of a number between 1 to 100. You will have to guess the number. You will be given lives according to your level of difficulty.")
difficulty_level = input("Which difficulty level do you ? Type 'easy' or 'hard': ").lower()
lives = 0
if difficulty_level == "easy":
  lives += 10
else:
  lives += 5

user_status = False

print(logo)
while not user_status and not lives == 0:
  print(f"You have {lives} attempts remaining to guess the answer.")
  user_guess = int(input("Make a Guess: "))
  if user_guess > number_chosen_by_computer:
    print("Too high.")
    lives -= 1
  elif user_guess < number_chosen_by_computer:
    print("Too low.")
    lives -= 1
  else:
    user_status = True
  if user_status == False and lives != 0:
    print("Guess again.")


print(logo)
if user_status == True:
  print(f"You got it! The answer was {number_chosen_by_computer}. \nYou Win.😃")
else:
  print(f"You have run out of guesses. The number was {number_chosen_by_computer}. You lose.😭")
