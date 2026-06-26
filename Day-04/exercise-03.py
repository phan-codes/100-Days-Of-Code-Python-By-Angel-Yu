# Dont change the code below

row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# Write your code below this line
first_digit = int(position[0])
second_digit = int(position[1])
map[second_digit - 1][first_digit - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")
