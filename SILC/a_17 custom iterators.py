#author: vikranth datta
#custom iterators
class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __str__(self):
        return "Name: " + self.name + " Author: " + self.name
    
    def __repr__(self):
        return "Name: " + self.name + " Author: " + self.name



class Backpack:
    def __init__(self, books):
        self.books = books

    def __str__(self):
        return books.__str()

    def __repr__(self):
        return books.__str()

    def __iter__(self):
        self.x = 0
        return self

    def __next__(self):
        if (self.x < len(self.books)):
            current_book = self.books[self.x]
            self.x = self.x+1
            return current_book
        else:
            raise StopIteration


# books
Book_1 = Book("	My Truth", "Indira Gandhi")
Book_2 = Book("	War and peace", "Leo Tolstoy")
Book_3 = Book("	Man and Superman", "G.B.Shaw")
Book_4 = Book("Invisible Man", "	H.G.Wells")
#create a list of Books
books = [Book_1,Book_2,Book_3, Book_4]

# creating an object
Backpack_1 = Backpack(books)

print("--> Calling internal iterator")
for x in Backpack_1:
    print(x)

iterator_x = iter(Backpack_1)
print("--> Calling explit iterator")
print(next(iterator_x))
print(next(iterator_x))
print(next(iterator_x))
