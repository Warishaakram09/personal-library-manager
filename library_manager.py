import os
import json

# -------------------- Load Library from File --------------------
def load_library():
    if os.path.exists("library.txt"):
        with open("library.txt", "r") as file:
            return json.load(file)
    return []

# -------------------- Save Library to File --------------------
def save_library(library):
    with open("library.txt", "w") as file:
        json.dump(library, file)

# -------------------- Add Book --------------------
def add_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_input = input("Have you read this book? (yes/no): ").lower()
    read_status = True if read_input == "yes" else False

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    }
    library.append(book)
    print("✅ Book added successfully!\n")

# -------------------- Remove Book --------------------
def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("✅ Book removed successfully!\n")
            return
    print("❌ Book not found!\n")

# -------------------- Search Book --------------------
def search_book(library):
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ")
    keyword = input("Enter the title/author to search: ").lower()

    matches = []
    for book in library:
        if (choice == "1" and keyword in book["title"].lower()) or \
           (choice == "2" and keyword in book["author"].lower()):
            matches.append(book)

    if matches:
        print("📚 Matching Books:")
        for idx, book in enumerate(matches, 1):
            status = "Read" if book["read"] else "Unread"
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("❌ No matching books found.\n")

# -------------------- Display All Books --------------------
def display_books(library):
    if not library:
        print("📭 Your library is empty.\n")
        return
    print("📚 Your Library:")
    for idx, book in enumerate(library, 1):
        status = "Read" if book["read"] else "Unread"
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    print()

# -------------------- Display Stats --------------------
def display_stats(library):
    total = len(library)
    if total == 0:
        print("No books in library.\n")
        return
    read_count = sum(1 for book in library if book["read"])
    percent = (read_count / total) * 100
    print(f"📊 Total books: {total}")
    print(f"📈 Percentage read: {percent:.1f}%\n")

# -------------------- Menu Loop --------------------
def menu():
    library = load_library()
    while True:
        print("""
📘 Welcome to your Personal Library Manager!
1. Add a book
2. Remove a book
3. Search for a book
4. Display all books
5. Display statistics
6. Exit
""")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_stats(library)
        elif choice == "6":
            save_library(library)
            print("💾 Library saved to file. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Try again.\n")

# -------------------- Run App --------------------
if __name__ == "__main__":
    menu()
