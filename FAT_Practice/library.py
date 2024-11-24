# 6. Library Book Management System (Dictionaries)
# Design a menu-driven program using user-defined functions to manage a library’s books, where each book is stored as a dictionary with its title as the key and author as the value. The program should allow the user to:
# - Add a new book with its title and author
# - Remove a book by title
# - Search for a book by its title and display the author
# - Update the author of a specific book
# - Display all books by a particular author
# - Display all available books (title and author) in the library
# - Count and display the total number of books in the library

library = {
    "To Kill a Mockingbird": "Harper Lee",
    "1984": "George Orwell",
    "Moby-Dick": "Herman Melville",
    "The Great Gatsby": "F. Scott Fitzgerald",
    "Pride and Prejudice": "Jane Austen"
}
library['Serendipity'] = "Ashok Ferry"
print(library)
del library['1984']
print(library)
print(library["Moby-Dick"])
print((library.items()))