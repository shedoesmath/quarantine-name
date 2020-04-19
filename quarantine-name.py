"""
This program asks the user how they are feeling and what they last
ate out of the cupboard and then generates the user's quarantine name.
"""


def main():
    """ Ask the user how they are feeling and what they last ate. """
    print("Let's play a fun game! Tell me how you're feeling and "
          "what you last ate, and I'll tell you your quarantine name.")
    my_feelings = input("How are you feeling? ")
    stress_food = input("What did you last eat from the cupboard? ")
    print("Your quarantine name is ", my_feelings, " ", stress_food, ".", sep='')


if __name__ == "__main__":
    main()
