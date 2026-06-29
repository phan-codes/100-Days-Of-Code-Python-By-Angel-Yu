# Write your code below this row
total = 0
for even_numbers in range(2, 101, 2):
   total += even_numbers

print(total)   

# Another method 
total_even = 0
for number in range(1, 101):
   if number % 2 == 0:
      total_even += number
print(total_even)