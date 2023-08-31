# Display the following menu to the user
# 1) create a new file
# 2) display the new file
# 3) add a new item to the file
# Make a selection 1, 2 or 3
# If they select anything other than 1, 2 and 3 then display the error message. If 
# they select 1 ask the user to enter a school subject and save it to new file which 
# is called " subject.txt ". If they select 2 then display the content of the " 
# subject.txt ". If they select 3 then ask the user to enter new subject and save it
# to the file and display the entire contents of the file.
print("Menu:")
print("1) Create a new file")
print("2) Display the new file")
print("3) Add a new item to the file")
while True:
 selection = input("Make a selection (1, 2, or 3): ")
 if selection == "1":
 subject = input("Enter a school subject: ")
 with open("subject.txt", "w") as file:
 file.write(subject)
 print("File created successfully!")
 elif selection == "2":
 try:
 with open("subject.txt", "r") as file:
 content = file.read()
 print("Content of the file:")
 print(content)
 except FileNotFoundError:
 print("File not found!")
 elif selection == "3":
 subject = input("Enter a new subject: ")
 try:
 with open("subject.txt", "a") as file:
 file.write("\n" + subject)
 print("Item added successfully!")
 with open("subject.txt", "r") as file:
 content = file.read()
 print("Content of the file:")
 print(content)
 except FileNotFoundError:
 print("File not found!")
 else:
 print("Error: Invalid selection!")
 choice = input("Do you want to continue? (Y/N): ")
 if choice.upper() != "Y":
 break


