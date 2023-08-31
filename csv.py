# using the Books.csv file, ask the user how many records they want to add to the list and then allow them to add that many, after all the data has been added, ask for an author and display all the books in the list by that author. if there are no books by that author in the list, display a suitable message.
num_records = int(input("How many records would you like to add? "))
with open("Books.csv", "a") as file:
    for _ in range(num_records):
        book = input("Enter the book title: ")
        author = input("Enter the author: ")
        year = input("Enter the year released: ")
        file.write(f"{book},{author},{year}\n")
search_author = input("Enter the author name to search for books: ")
with open("Books.csv", "r") as file:
    lines = file.readlines()
    found_books = False
    for line in lines:
        book, author, year = line.strip().split(",")
        if author.lower() == search_author.lower():
            print(f"Book: {book}, Author: {author}, Year Released: {year}")
            found_books = True
    if not found_books:
        print("No books found by the specified author.")

# using the Books.csv file, ask the user to enter a starting year and end year. Display all books releaded between those two year.
start_year = int(input("Enter the starting year: "))
end_year = int(input("Enter the ending year: "))
with open("Books.csv", "r") as file:
    lines = file.readlines()
    found_books = False
    for line in lines:
        book, author, year = line.strip().split(",")
        if start_year <= int(year) <= end_year:
            print(f"Book: {book}, Author: {author}, Year Released: {year}")
            found_books = True
    if not found_books:
        print("No books found within the specified years.")

