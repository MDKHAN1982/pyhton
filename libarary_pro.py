# book = current , books = actual book, 
# 1. display book, 2. Borrow book 3.return book
class library:
    def __init__(self, books):
        self.books=books
    def display_book(self):
        for book in self.books:
            print(book)
    def borrow_book(self,borrow_book):
        if borrow_book in self.books:
            print("GET your book : ")
            self.books.remove(borrow_book)
        else:
            print("Book not available")
       
    def return_book(self,return_book):
        print("Enter book to return:")
        self.books.append(return_book)


books= [ 'c' , 'c++' ,'java' ,'python']
msg='''
1.Display book
2. Borrow book
3. Return book
'''
o=library(books)


while True:
    print(msg)
    ch = int(input("Enter your choise: "))
    if ch==1:
        o.display_book()
    elif ch == 2:
        book=input("Enter Book Name:")
        o.borrow_book(book)
    elif ch==3:
        book=input("Enter book to return:")
        o.return_book(book)
    else:
        print (" Thank you for using public libarary ")
        quit()



