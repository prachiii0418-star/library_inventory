from library_manager import Book, LibraryInventory


def menu():
    print("\n======= Library Management System =======")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search Book")
    print("6. Exit")
    print("========================================")


def main():
    inventory = LibraryInventory()

    while True:
        menu()
        try:
            choice = int(input("Enter your choice: "))
        except:
            print("Invalid input! Enter a number from 1–6.")
            continue

        if choice == 1:
            title = input("Enter book title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            try:
                inventory.add_book(Book(title, author, isbn))
                print("Book added successfully!")
            except Exception as e:
                print("Error:", e)

        elif choice == 2:
            isbn = input("Enter ISBN to issue: ")
            book = inventory.search_by_isbn(isbn)
            if not book:
                print("Book not found.")
            else:
                try:
                    book.issue()
                    inventory.save_to_file()
                    print("Book issued!")
                except Exception as e:
                    print("Error:", e)

        elif choice == 3:
            isbn = input("Enter ISBN to return: ")
            book = inventory.search_by_isbn(isbn)
            if not book:
                print("Book not found.")
            else:
                try:
                    book.return_book()
                    inventory.save_to_file()
                    print("Book returned!")
                except Exception as e:
                    print("Error:", e)

        elif choice == 4:
            books = inventory.display_all()
            if not books:
                print("No books in library.")
            for b in books:
                print(b)

        elif choice == 5:
            title = input("Enter title keyword: ")
            results = inventory.search_by_title(title)
            if not results:
                print("No matching books found.")
            for b in results:
                print(b)

        elif choice == 6:
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Select from 1–6 only.")


if __name__ == "__main__":
    main()
