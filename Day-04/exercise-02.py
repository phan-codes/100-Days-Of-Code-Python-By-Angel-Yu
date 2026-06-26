import random

# Dont change the code below
test_seed = int(input("Create a seed number: \n"))
random.seed(test_seed)

# Split string method
namesAsCSV = input("Give me everybody's names, seperated by a comma. \n")
names = namesAsCSV.split(", ")

# Write your code below this line

random_number = random.randint(0, len(names) - 1)
payer = names[random_number]



# Using random.choice for less code

payer = random.choice(names)

print(f"{payer} is going to  buy the meal today!")