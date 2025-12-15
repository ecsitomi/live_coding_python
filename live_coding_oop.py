'''
Feladat: Könyvtár kezelő rendszer

Készíts egy Book (Könyv) osztályt és egy Library (Könyvtár) osztályt.

Book osztály követelmények:
- Attribútumok: title (cím), author (szerző), isbn (ISBN szám), available (elérhető-e, alapból True)
- Metódusok:
  - __init__: inicializálás
  - __str__: szöveges reprezentáció (pl: "Cím by Szerző (ISBN: ...)")
  - borrow(): kikölcsönzés - available legyen False, ha már ki van kölcsönözve, return False
  - return_book(): visszahozás - available legyen True

Library osztály követelmények:
- Attribútumok: name (könyvtár neve), books (könyvek listája, kezdetben üres)
- Metódusok:
  - __init__: inicializálás
  - add_book(book): könyv hozzáadása
  - remove_book(isbn): könyv eltávolítása ISBN alapján
  - find_book(title): könyv keresése cím alapján (return a book objektum vagy None)
  - list_available_books(): listázza az elérhető könyveket
  - borrow_book(isbn): kikölcsönzés ISBN alapján

Bónusz (ha maradt idő):
- Implementálj számláló funkciót: hány könyv van összesen, hány elérhető
- Error handling: mi van, ha nem létező könyvet próbálunk törölni/kikölcsönözni?

Teszteld a kódot példa adatokkal!
'''

# Book osztály - Egy könyvet reprezentál
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
    
    def __str__(self):
        status = "Elérhető" if self.available else "Kikölcsönözve"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"
    
    def borrow(self):
        if not self.available:
            return False
        self.available = False
        return True
    
    def return_book(self):
        self.available = True


# Library osztály - Könyvtárat kezel
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                return True
        return False
    
    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
    
    def list_available_books(self):
        available = []
        for book in self.books:
            if book.available:
                available.append(book)
        return available
    
    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.borrow():
                    return True
                else:
                    return False
        return False


# TESZT
# Könyvtár létrehozása
library = Library("Városi Könyvtár")

# Könyvek létrehozása
book1 = Book("Harry Potter", "J.K. Rowling", "123")
book2 = Book("1984", "George Orwell", "456")
book3 = Book("Python alapok", "Guido van Rossum", "789")

# Könyvek hozzáadása
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Elérhető könyvek listázása
print("=== Elérhető könyvek ===")
for book in library.list_available_books():
    print(book)

print("\n=== Kikölcsönzés ===")
# Könyv kikölcsönzése
if library.borrow_book("123"):
    print("Harry Potter sikeresen kikölcsönözve")
else:
    print("Nem sikerült kikölcsönözni")

# Elérhető könyvek listázása újra
print("\n=== Elérhető könyvek kikölcsönzés után ===")
for book in library.list_available_books():
    print(book)

# Könyv keresése
print("\n=== Könyv keresése ===")
found_book = library.find_book("1984")
if found_book:
    print(f"Megtalálva: {found_book}")

# Könyv visszahozása
print("\n=== Visszahozás ===")
book1.return_book()
print("Harry Potter visszahozva")

# Elérhető könyvek listázása
print("\n=== Elérhető könyvek visszahozás után ===")
for book in library.list_available_books():
    print(book)