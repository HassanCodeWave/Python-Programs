# program to ask the user to enter a number between 10 and 20. if 
# they enter a number between these ranges then display the message " 
# Thankyou ", otherwise display the message " Incorrect Answer "
num = int(input("Enter a number between 10 and 20: "))
if num >= 10 and num <= 20:
print("Thank you")
else:
print("Incorrect Answer")

# program to ask the user's age if they are 18 or above, display 
# the message " You can vote ", if they aged 17, display the message " 
# You can learn to drive " if they are aged 16, display the message " 
# You can buy a lottery ticket ", if they are under 16, display the 
# message " You can go trick or treating "
age = int(input("Enter your age: "))
if age >= 18:
print("You can vote.")
elif age == 17:
print("You can learn to drive.")
elif age == 16:
print("You can buy a lottery ticket.")
else:
print("You can go trick or treating.")

# Ask the user to enter 1,2,3 if they enter 1 display the message 
# "Thank you", if they enter 2, display the message " Well done ", if 
# they enter 3, display the message " Correct ", if they enter other 
# number than display the message " Error Message "
num = int(input("Enter a number (1, 2 or 3): "))
if num == 1:
print("Thank you.")
elif num == 2:
print("Well done.")
elif num == 3:
print("Correct.")
else:
print("Error message.")

# write a program in python in which Take input of five subjects marks 
# obtained, Sum up the marks, Grade the marks as below, obtained marks 
# is = > 90 and < = 101 Grade "A+", obtained marks is = > 80 and < = 90 
# Grade "A", obtained marks is = > 70 and < = 80 Grade "B"
n = input( "Enter your name :")
n1 = int(input("Enter your maths marks:"))
n2 = int(input("Enter your physics marks:"))
n3 = int(input("Enter your computer marks:"))
n4 = int(input("Enter your english marks:"))
n5 = int(input("Enter your chemistry marks:"))
total_marks = n1 + n2 + n3 + n4 + n5
print("Total Marks",total_marks)
percentage = ( total_marks * 100 ) / 500
print("Total Percentage",percentage) 
if percentage >= 90 and percentage <=100 : 
print(" Your grade is 'A +' " ) 
elif percentage >= 80 and percentage <=90 : 
print(" Your grade is 'A' " ) 
elif percentage >= 70 and percentage <80 : 
print(" Your grade is 'B' " ) 
elif percentage >= 60 and percentage <70 : 
print(" Your grade is 'B' " ) 
else
print( "You are Failed")