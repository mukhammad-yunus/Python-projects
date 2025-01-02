# from random import randint

# def roll_dice(amount: int = 2)->list[int]:
#   if amount <= 0:
#     raise ValueError
#   rolls: list[int] = []
#   for i in range(amount):
#     random_roll: int = randint(1, 6)
#     rolls.append(random_roll)

#   return rolls

# def main():
#   while True:
#     try:
#       user_input: str = input('How many dice would you like to roll? (Or for quit type "exit"): ')
#       if user_input.lower() == 'exit':
#         print("Thanks for playing!")
#         break
#       print(*roll_dice(int(user_input)), sep=", ")
#     except ValueError:
#       print("(Please enter a valid number)")

# if __name__ == '__main__':
#   main()

from random import randint

def roll_dice(amount: int = 2) -> tuple[list[int], int]:
  if amount <= 0:
    raise ValueError
  rolls: list[int] = []
  rolls_sum: int = 0
  for i in range(amount):
    random_num: int = randint(1, 6)
    rolls_sum += random_num
    rolls.append(random_num)
  return rolls, rolls_sum

def main():
  while True:
    try:
      user_input: str = input('How many dice would you like to roll? (Or for quit type "exit"): ')
      if user_input.lower() == 'exit':
        print('Thanks for playing!')
        break
      # print(roll_dice(int(user_input)))
      dices, dices_sum = roll_dice(int(user_input))
      print(f"The dices are {', '.join(map(str, dices))}")
      print("The sum of all dices are ", dices_sum)
    except ValueError:
      print("(Please enter a valid value)")

if __name__ == "__main__":
  main()
  # when the script is run directly, __name__ is set to "__main__". if the script is imported it is not set to "__main__". that means, if you run the script directly main() is called


# WHAT DID I LEARN:
# -> indicates what type of return should be. if -> int, return should be integer, so on.
# raise ValueError raises an error on purpose.
# return a, b returns a tuple element, value of a being 0 index and value of b being 1 index. It is really handy when you have to return more than one data, since tuples are immutable
# UNPACKING: if you have a list or a tuple with one or more elements in it, e.g example= [ a, b, c] or example =(a, b, c), you can access and create a variable like name1, name2, name3 = example. name1 = example[0], name2 = example[1] and finally name3 = example[2]
# .map(function, iterable) iterates the function to a iterable data and returns a map object containing the result.
# separator.join(iterable), it joins iterable and makes all together by using separator. e.g output of ", ".join(['apple', 'banana', 'orange]) is "apple, orange, banana"
