class Book():
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def show(self):
        print(f"title:{self.title},author:{self.author}")
book1 = Book("To Kill a Mockingbird", "Harper Lee")
book2 = Book("1984", "George Orwell")
book3 = Book("The Alchemist", "Paulo Coelho")
print(book1.title, book1.author)
print(book2.title, book2.author)
print(book3.title, book3.author)