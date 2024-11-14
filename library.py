import random

# Add a new book with its title and author
def addBook(library, title, author):
    library[title] = author
    print(f"Book '{title}' by {author} added.")
    return library

# Remove a book by title
def removeBook(library, title):
    if title in library:
        del library[title]
        print(f"Book '{title}' removed.")
    else:
        print(f"Book '{title}' not found.")
    return library

# Search for a book by its title and display the author
def searchBook(library, title):
    author = library.get(title)
    if author:
        print(f"Book '{title}' is written by {author}.")
    else:
        print(f"Book '{title}' not found.")

# Update the author of a specific book
def updateAuthor(library, title, new_author):
    if title in library:
        old_author = library[title]
        library[title] = new_author
        print(f"Author of '{title}' updated from {old_author} to {new_author}.")
    else:
        print(f"Book '{title}' not found.")
    return library

# Display all books by a particular author
def displayBooksByAuthor(library, author):
    books = [title for title, book_author in library.items() if book_author == author]
    if books:
        print(f"Books by {author}: {', '.join(books)}")
    else:
        print(f"No books found by {author}.")

# Display all available books (title and author) in the library
def displayAllBooks(library):
    if library:
        print("All books in the library:")
        for title, author in library.items():
            print(f"Title: {title}, Author: {author}")
    else:
        print("No books in the library.")

# Count and display the total number of books in the library
def countBooks(library):
    total_books = len(library)
    print(f"Total number of books in the library: {total_books}")
    return total_books

library = {
    "To Kill a Mockingbird": "Harper Lee",
    "1984": "George Orwell",
    "Moby-Dick": "Herman Melville",
    "The Great Gatsby": "F. Scott Fitzgerald",
    "Pride and Prejudice": "Jane Austen"
}

book_to_add = "The Catcher in the Rye"
author_to_add = "J.D. Salinger"
book_to_remove = "1984"
book_to_search = "Moby-Dick"
book_to_update = "The Great Gatsby"
new_author = "A. F. Fitzgerald"
author_to_display = "Harper Lee"

while True:
    print("\nLibrary Book Management Menu")
    print("1: Add a new book with its title and author")
    print("2: Remove a book by title")
    print("3: Search for a book by its title and display the author")
    print("4: Update the author of a specific book")
    print("5: Display all books by a particular author")
    print("6: Display all available books in the library")
    print("7: Count and display the total number of books in the library")
    
    choice = random.randint(1, 7)

    if choice == 1:
        print(f"Adding book '{book_to_add}' by {author_to_add}.")
        addBook(library, book_to_add, author_to_add)
        break
    elif choice == 2:
        print(f"Removing book '{book_to_remove}'.")
        removeBook(library, book_to_remove)
        break
    elif choice == 3:
        print(f"Searching for book '{book_to_search}'.")
        searchBook(library, book_to_search)
        break
    elif choice == 4:
        print(f"Updating author for book '{book_to_update}' to {new_author}.")
        updateAuthor(library, book_to_update, new_author)
        break
    elif choice == 5:
        print(f"Displaying all books by {author_to_display}.")
        displayBooksByAuthor(library, author_to_display)
        break
    elif choice == 6:
        displayAllBooks(library)
        break
    elif choice == 7:
        countBooks(library)
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
        choice = random.randint(1, 7)
