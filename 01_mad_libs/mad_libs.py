def get_input(word_type: str):
  user_input: str = input(f"Enter a {word_type}: ")
  return user_input

adjective1 = get_input("adjective")
adjective2 = get_input("adjective")
noun1 = get_input("noun")
noun2 = get_input("plural noun")
noun3 = get_input("noun")
verb1 = get_input("verb ending -ng")
noun4 = get_input("noun")
adjective3 = get_input("adjective")


story = f"""
Yesterday, I decided to cook {adjective1} pasta for my {adjective2} friends. I grabbed a {noun1} instead of a spoon and started stirring the {noun2} in a pot. Suddenly, the {noun3} I was babysitting jumped into the pot and started {verb1}!

I panicked and threw {noun4} at it, but it only made things {adjective3}.
"""
print(story)


# in this project, I learned type annotation ":". e.g word_type: str means the variable should be a string.
# also i learned f string.  