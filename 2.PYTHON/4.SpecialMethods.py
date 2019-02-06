class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # Método especial -> Método que convierte a string el objeto. Tb hay otro que es __str__
    def __repr__(self):
        return f"Title: {self.title}, Author: {self.author}"

    # Método especial
    def __len__(self):
        return self.pages


myBook = Book("Python", "Jose", 250)
print(myBook)
length_book = len(myBook)
print(length_book)
