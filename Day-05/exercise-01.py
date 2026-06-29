# Dont change the code below
student_heights = input("Input a list of student heights \n").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

print(student_heights)



# Write your code below this line

total = 0
length = 0
average = 0

for height in student_heights:
    total += height
    length += 1
    average = round(total / length)
   
    
print(average) 