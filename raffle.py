# raffle)
import time
import random
# List of people entered in to raffle
people = []

# Get details of item being raffled
raffle_item = input("What is being raffled?")


# Get names of people entering
ask_again = True
while ask_again == True:
    name = input("what is your name")
    if name == "end":
        ask_again = False
    else:
        people.append(name)
winner =random.randit(0,participant_number)
print(people[winner])
