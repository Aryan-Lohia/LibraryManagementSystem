from Library import *
from password_system import *
if __name__ == "__main__":
    bookslist=[]
    library_name = "Aryan's Library"
    OWNER = LibraryClass(bookslist, library_name)
    print(f"Welcome to {library_name}\n")
    while (True):
        authentication = False

        while(not authentication):
            user_name = (input("Please enter user's name\n")).upper().lstrip().rstrip()
            authentication=password_sys(user_name)

        print(f"Welcome {user_name}\n")
        OWNER.Display_book()
        while (True):
            print(
                "\nWhat would you like to do now?\nPress 1 to display booklist again\nPress 2 to search for a book in the booklist\nPress 3 to borrow a book\nPress 4 to return a book\nPress 5 to add a book to the booklist\nPress 6 to display your borrowed books\nPress q to quit\n")
            choice = input()
            if (choice.upper() != 'Q'):
                OWNER.User_choice( int(choice), user_name)
            else:
                break
        print("For Next User, Press 1. To quit library, press any other key\n")
        if (input() == '1'):
            continue
        break
    if OWNER.borrowers_index:
        print("Books Not returned are:")
        print("Borrower\t\tBooks")
        for borrower,books in OWNER.borrowers_index.items():
            print(f"{borrower}\t\t\t", end="")
            for book in books:
                print(f"{book} , ", end="")
            print("\b\b")













