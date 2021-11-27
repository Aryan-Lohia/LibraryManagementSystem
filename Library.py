class Library:

    def __init__(self, bookslist, library_name) -> None:
        self.booklist = {}
        for books in bookslist:
            self.booklist[books.upper()]="AVAILABLE"
        self.library_name = library_name
        self.borrowers_index = {}

    def Display_book(self) -> None:
        print(f"Books in {self.library_name}:")
        i=1
        for books in self.booklist:
            print(f"{i}.{books}")
            i+=1

    def Lend_book(self, borrowers_name, book_serial) -> None:
        books=list(self.booklist.keys())
        try:
            book_name = books[book_serial-1]
        except:
            print(f"Invalid serial no. Please choose a book from the list.\n")
            return
        if self.booklist[book_name]=="LENDED":
            print(f"Sorry {borrowers_name}. {book_name} has already been lended to ", end="")
            for borrower in self.borrowers_index:
                if book_name in self.borrowers_index[borrower]:
                    if borrowers_name==borrower:
                        print("you")
                    else:
                        print(borrower)
                    break

        elif book_name in self.booklist:
            print(f"{book_name} has been lended to {borrowers_name}\n")

            if borrowers_name in self.borrowers_index.keys():
                self.borrowers_index[borrowers_name].append(f"{book_name}")
            else:
                self.borrowers_index[borrowers_name] = [f"{book_name}"]
            self.booklist[book_name]="LENDED"

    def View_Borrowed(self,borrowers_name) -> None:
        if borrowers_name in self.borrowers_index.keys():
            print("These are the books you have borrowed:")
            borrowers_booklist = self.borrowers_index[borrowers_name]
            for i, books in enumerate(borrowers_booklist):
                print(f"{i + 1}.{books}")
                return 1
        else:
            print("You have not borrowed any books as of now.\n")
            return 0
    def Return_book(self, borrowers_name) -> int:
        if (self.View_Borrowed(borrowers_name)==1):
            try:
                choice = int((input("Please input serial number of the book would you like to return?\n"))[0])
                returned_book = borrowers_booklist[choice - 1]
                print(f"{borrowers_name} has returned {returned_book}\n")
                self.booklist[returned_book] = "AVAILABLE"
                borrowers_booklist.pop(choice - 1)
                if (not self.borrowers_index[borrowers_name]): del self.borrowers_index[borrowers_name]
            except:
                print("Please enter a valid serial number and try again\n")

    def Add_book(self, book_name) -> None:

        if book_name not in self.booklist:
            self.booklist[book_name]="AVAILABLE"
            with open("books.txt", "a") as books:
                books.write(f"\n{book_name}")
            print("Your Book has been added. \nThank You for contributing to this library\n")
        else:
            print("This book already exists in library\n")

    def Search_book(self, book_name) -> None:
        if book_name in self.booklist:
            print(f"{book_name} is present in library at serial number {list(self.booklist.keys()).index(book_name)+1}\n")
        elif True in map(lambda x:book_name in x,list(self.booklist.keys())):
            print("Closest Results:")
            for book in self.booklist:
                if book_name in book:
                    print(f"{book} : present in library at serial number : {list(self.booklist.keys()).index(book)+1}")
        else:
            print("Sorry the book you need is not present in the library\n")


def execute(obj, choice, user_name) -> None:
    if choice == 1:
        obj.Display_book()
    elif choice == 2:
        book = (input("Enter Name of book you want to search:\n")).upper()
        obj.Search_book(book)
    elif choice == 3:
        book = int(input("Enter serial number of book you want to borrow:\n"))
        obj.Lend_book(user_name, book)
    elif choice == 4:
        obj.Return_book(user_name)
    elif choice == 5:
        book = (input("Enter Name of book you want to add:\n")).upper()
        obj.Add_book(book)
    elif choice==6:
        obj.View_Borrowed(user_name)
    else:
        print("Invalid Entry. Please try again")

if __name__ == "__main__":
    bookslist=[]
    with open("books.txt") as books:
        while (True):
             book = (books.readline().strip("\n"))
             if (len(book) ==0):
                break
             bookslist.append(book)
    library_name = input("Enter a name for your library:\n")
    OWNER = Library(bookslist, library_name)
    print(f"Welcome to {library_name}\n")
    while (True):
        user_name = (input("Please enter user's name\n")).upper()
        print(f"Welcome {user_name}\n")
        OWNER.Display_book()
        while (True):
            print(
                "\nWhat would you like to do now?\nPress 1 to display booklist again\nPress 2 to search for a book in the booklist\nPress 3 to borrow a book\nPress 4 to return a book\nPress 5 to add a book to the booklist\nPress 6 to display your borrowed books\nPress q to quit\n")
            choice = input()
            if (choice.upper() != 'Q'):
                execute(OWNER, int(choice), user_name)
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
            print(f"{borrower}\t\t\t",end="")
            for book in books:
                print(f"{book} , ", end="")
            print("\b\b")
















