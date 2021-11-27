class Library:

    def __init__(self, bookslist, library_name) -> None:
        self.booklist = {}
        with open("books.txt") as books:
            while (True):
                book = (books.readline().strip("\n"))
                if (len(book) ==0):
                    break
                bookslist.append(book)
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


    def execute(self, choice, user_name) -> None:
        if choice == 1:
            self.Display_book()
        elif choice == 2:
            book = (input("Enter Name of book you want to search:\n")).upper()
            self.Search_book(book)
        elif choice == 3:
            book = int(input("Enter serial number of book you want to borrow:\n"))
            self.Lend_book(user_name, book)
        elif choice == 4:
            self.Return_book(user_name)
        elif choice == 5:
            book = (input("Enter Name of book you want to add:\n")).upper()
            self.Add_book(book)
        elif choice==6:
            self.View_Borrowed(user_name)
        else:
            print("Invalid Entry. Please try again")

















