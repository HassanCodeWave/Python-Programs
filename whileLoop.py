# Ask the user to enter a and then enter another number. add these two numbers 
# together and then ask if they want to add another number. if they enter "Y", ask 
# them to enter another number and keep adding numbers until they do not 
# answer "Y".once the loop has stopped, display the total.
a = int(input("Enter a number: ")) 
total = a 
while True:
b = int(input("Enter another number: ")) 
total += b 
choice = input("Do you want to add another number? (Y/N): ") 
if choice.upper() != "Y":
break 
print("The total is:", total)

# Create a variable called compnum and set the value to 50. ask the user to 
# enter a while their guess is not the same as the compnum value, tell them if 
# their guess is too low or too high and ask them to have another guess, if they 
# enter the same value as compnum then display the message " WELLDONE"
compnum = 50 
while True:
guess = int(input("Guess the number: ")) 
if guess < compnum:
print("Too low!")
elif guess > compnum:
print("Too high!")
else:
print("WELLDONE!")
break 

# Ask the user to enter number between 10 and 20, if they enter a value under 
# 10, display the message "Too low" and ask them to try again. if they enter 
# value above 20 display the message "Too high" and ask them to try again and 
# keep using the same until they enter a value that is between 10 and 20 then 
# display the message " Thankyou" 
number = 0 
while True:
number = int(input("Enter a number between 10 and 20: ")) 
if number < 10:
print("Too low!")
elif number > 20:
print("Too high!")
else:
break 
print("Thank you!")

# Find out the factorial of a given number using while loop.
a = int(input("Enter any number : ")) 
i = a
t = 1
while i > 0:
t = i*t
i = i-1
print(t)
Result