from abc import ABC ,abstractmethod
class Book(ABC):
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.available=True
    @abstractmethod
    def borrow(self,book):
        pass
    @abstractmethod
    def return_book(self,book):
        pass
class PhysicalBook(Book):
    def borrow(self,book):
        #self.books.remove(book)
        self.available=False
        return f"{self.title} is borrowed"
    def return_book(self,book):
        #self.books.append(book)
        self.available=True
        return f"{self.title} is returned"
class Member:
    def __init__(self,name,member_id):
        self.name=name
        self.member_id=member_id
        self.borrowed_books=[]
    def borrow(self,book):
        if book.available:
            book.borrow(book)
            self.borrowed_books.append(book)
            return f"{book.title} is borrowed by {self.member_id}"
        else:
            return f"{self.title} is borrowed"
    def return_book(self,book):
        self.available=True
        self.borrowed_books.remove(book)
        return f"{self.member_id} has returned {book}"
        
class Library:
    def __init__(self,name):
        self.name=name
        self.books=[]
        self.members=[]
    def add_books(self,book):
        self.books.append(book)
    def add_member(self,member):
        self.members.append(member)
    def show_available_books(self):
        print("\n---Available Books---")
        for book in self.books:
            if book.available:
                print(f"[{book.title}] by {book.author}")
#Make a Book and Member object and add them to the library class
b1=PhysicalBook("How to get rich","Abdirahman Ahmed",1234)
b2=PhysicalBook("Winner Winner","Hamdi Ahmed",5678)

#member Object
m1=Member("Abdi","m001")
m2=Member("Khalid","m002")

#Make a Library Object and add memebers and books
l1=Library("Nairobi National Library")
l1.add_books(b1)
l1.add_books(b2)
l1.add_member(m1)
l1.add_member(m2)
#Test Our program
m1.borrow(b1)
l1.show_available_books()
m1.return_book(b1)
l1.show_available_books()