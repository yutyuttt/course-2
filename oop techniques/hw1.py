class Book:
    def __init__(self, title, authors, publication_year):
        self.title = title
        self.authors = authors
        self.publication_year = publication_year

    def __str__(self):
        auth = ' & '.join(self.authors)
        return f'{auth}: {self.title} ({self.publication_year})'

    def num_authors(self):
        return len(self.authors)


book1 = Book('Introduction to Algorithms (3rd ed.)', ['Cormen', 'Leiserson', 'Rivest', 'Stein'], 2009)
book2 = Book('Lauren Ipsum: A Story About Computer Science and Other Improbable Things', ['Bueno'], 2014)
book3 = Book('How Linux Works, 3rd Edition: What Every Superuser Should Know', ['Ward'], 2021)
book_list = [book1, book2, book3]

for book in book_list:
    print(book)

print()

# sorting order of book_list
book_list = [book3, book1, book2] # scramble order
book_list.sort(key=Book.num_authors, reverse=True)
for book in book_list:
    print(book)