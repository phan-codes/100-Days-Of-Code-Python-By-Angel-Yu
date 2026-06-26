import random

# Dont change the code below 
test_seed = int(input("Create a seed number: \n"))
random.seed(test_seed)

# Write your code below this line
random_number = random.randint(0, 1)

if random_number == 0: 
    print("Tails")
else:
    print("Heads")