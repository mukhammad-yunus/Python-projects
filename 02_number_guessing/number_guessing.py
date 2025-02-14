from random import randint

lower_num, higher_num = 1, 100
random_num: int = randint(lower_num, higher_num)
print(f'Guess the number in the range from {lower_num} to {higher_num}.')

attempts = 0
while True:
  try:
    user_guess: int = int(input("Guess: "))
    attempts +=1 #if the user enters an input with type of not int, the error occurs and attempt is not counted
  except ValueError as e:
    print("Please enter a valid number!")
    continue
  if user_guess > random_num:
    print(f"The number is less than {user_guess}")
  elif user_guess < random_num:
    print(f"The number is greater than {user_guess}")
  elif user_guess == random_num:
    print(f"You guessed it! The number is indeed {random_num}. You found the number in {attempts} {"attempt" if attempts ==1 else "attempts"}.")
    break


#   WHAT I LEARNED?
# randint takes two arguments: max and min of a range, including both.
# try and except. when there is a possibility of an error, this is useful. Also inside of try when an error happens, element/logic below that error get not executed,
# ternary conditional expression. it is too handy. the syntax is "value_if_true if condition else value_if_false"
