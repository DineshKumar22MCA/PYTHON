class library:
    def __init__(self,books):
        self.books=books

    def display_books(self):
        print(self.books)

    def barrow_books(self,x):
        if x in self.books:
            print("collect your book")
            self.books.remove(x)
        else:
            print("book is not available")

    def return_books(self,y):
        self.books.append(y)
        print("book is returned")

book=['c','c++','java','python']
o=library(book)
msg="""
     1.display books
     2.barrow books
     3.return books
     4. which option did you want select 
     5.do you want select enter 4
"""
while True:
    print(msg)
    choise=int(input("enter the number"))
    if choise==1:
        print("display books")
        o.display_books()
    elif choise==2:
        print("enter your book name")
        x=input("name")
        o.barrow_books(x)
    elif choise==3:
        print("enter your book name")
        y=input("name")
        o.return_books(y)
    elif choise > 3:
        print('thanking you')
        quit()
    else:
        print("thanking you")
        quit()