# program to ask a user to enter a number between 1 and 12 and 
# then display the time’s tables for that number
a = int(input('Enter Number Between 1 and 12'))
if a >= 1 and a <=12:
 for i in range(10):
 t = a * (i + 1)
 print(a,'times',i+1,'=',t)
else:
 print('Number must be between 1 and 12')

# Write a program to ask for a number below 50 and then count down 
# from 50 to that number, making sure you show the number they 
# entered in the output
a = int(input('Enter number below 50 '))
if a < 50 and a > 0:
 print(f"Countdown to {a}")
 for i in range(50,a-1,-1):
 print(i)
else:
 print('Number must be between 0 and 50')

# Ask the user set a variable called total to 0. ask the user to enter five 
# numbers and after each input ask them if they want that number 
# included, if they do, then add the number to the total if they do not 
# want it included, do not add it to the total. after they have entered 
# all five numbers, display the total. 
total = 0
count = 0
while count < 5:
 number = float(input("Enter a number: "))
 include = input("Do you want to include this number? (Y/N): ")
 if include.upper() == "Y":
 total += number
 count += 1
print("The total of included numbers is:", total)

# write a program and ask how many people the user wants to invite 
# to a party. if they enter a number below 10, ask for names, and after 
# each name display " Names " has been invited. if they enter a 
# number that is 10 or higher, display the message " Too many people 
# people "
a = int(input('Enter number of peoples to invite'))
if a < 10 and a > 0:
 for i in range(a):
 b = input('Enter name of the person')
 print(f"{b} has been invited to the party")
elif a > 10:
 print('Too many people')
else:
 print('Invalid number')