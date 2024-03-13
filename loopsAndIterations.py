# Loops and Iterations. For/While loops

nums = [1, 2, 3, 4, 5]

print('For loop through a list called nums'.upper())
for num in nums: #Loops through the list called nums
	print(num)

# Break and Continue statements in loops
print('Usage of \'Break\' condition in For loop'.upper())
for num in nums:
	if num == 3:
		print('Found!')
		break	#Break statement - Breaks out of a loop when a condition is met
	print(num)

print('Usage of \'Continue\' condition - For loop'.upper())
for num in nums:
	if num == 3:
		print('Found!')
		continue #Continue statement - Continues throught the rest of the loop after a condition is met
	print(num)

#Loop within a loop
print('Usage of \'Nested Loop\' - For loop'.upper())
for num in nums:
	for letter in 'ab': #Be careful with nested loops as they can go through a lot of combinations.
		print(num, letter)

#Loop a certain number of times that can be defined
print('Usage of for loop where the end range is defined'.upper())
for i in range(10):
	print(i)

print('Usage of for loop where the start and end range is defined'.upper())
for i in range(1,11):
	print(i)

#While loops - While loops keeps on going until a certail condition is met
print('While loop basic usage'.upper())

x = 0

while x < 10:
	print(x)
	x += 1

print('Break usage in while loop'.upper())

x = 0

while x < 10:
	if x == 5:
		break
	print(x)
	x += 1

print('Another way of the same code from above'.upper())

x = 0

while True:
	if x == 5:
		break
	print(x)
	x += 1

#Infinite Loop - Use ctrl + C to break
# print('Infinite Loop test'.upper())

# x = 0

# while True:
# 	print('Use ctrl + c to break this loop')
# 	print(x)
# 	x += 1