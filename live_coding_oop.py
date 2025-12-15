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

###################
##################
#################
################
###############

'''Dekorátorok és *args és **kwargs használata: '''

# DEKORÁTOR - Logolás
def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] {func.__name__} metódus meghívva")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} befejezve, eredmény: {result}")
        return result
    return wrapper


# Book osztály
class Book:
    def __init__(self, title, author, isbn, **kwargs):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
        # Plusz opcionális attribútumok **kwargs-ból
        self.year = kwargs.get('year', None)
        self.genre = kwargs.get('genre', None)
        self.pages = kwargs.get('pages', None)
    
    def __str__(self):
        status = "Elérhető" if self.available else "Kikölcsönözve"
        base = f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"
        extras = []
        if self.year:
            extras.append(f"Év: {self.year}")
        if self.genre:
            extras.append(f"Műfaj: {self.genre}")
        if extras:
            base += f" [{', '.join(extras)}]"
        return base
    
    @log_action
    def borrow(self):
        if not self.available:
            return False
        self.available = False
        return True
    
    @log_action
    def return_book(self):
        self.available = True
        return True


# Library osztály
class Library:
    def __init__(self, name, *initial_books):
        self.name = name
        # *args használata - több könyvet kaphat inicializáláskor
        self.books = list(initial_books)
    
    @log_action
    def add_book(self, book):
        self.books.append(book)
        return True
    
    def add_multiple_books(self, *books):
        """*args használat - több könyv hozzáadása egyszerre"""
        for book in books:
            self.books.append(book)
        print(f"{len(books)} könyv hozzáadva")
    
    @log_action
    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                return True
        return False
    
    def find_book(self, **search_params):
        """**kwargs használat - keresés több szempont alapján"""
        results = []
        for book in self.books:
            match = True
            if 'title' in search_params:
                if book.title.lower() != search_params['title'].lower():
                    match = False
            if 'author' in search_params:
                if book.author.lower() != search_params['author'].lower():
                    match = False
            if 'isbn' in search_params:
                if book.isbn != search_params['isbn']:
                    match = False
            if 'genre' in search_params and book.genre:
                if book.genre.lower() != search_params['genre'].lower():
                    match = False
            if match:
                results.append(book)
        return results
    
    def list_available_books(self):
        available = []
        for book in self.books:
            if book.available:
                available.append(book)
        return available
    
    @log_action
    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book.borrow()
        return False
    
    def get_stats(self):
        """Statisztika a könyvtárról"""
        total = len(self.books)
        available = len(self.list_available_books())
        borrowed = total - available
        return {
            'total': total,
            'available': available,
            'borrowed': borrowed
        }


# TESZT
print("=== Könyvtár létrehozása kezdő könyvekkel (*args) ===")
book1 = Book("Harry Potter", "J.K. Rowling", "123", year=1997, genre="Fantasy")
book2 = Book("1984", "George Orwell", "456", year=1949, genre="Dystopia")

# *args használat - több könyvet adunk át inicializáláskor
library = Library("Városi Könyvtár", book1, book2)

print("\n=== Több könyv hozzáadása egyszerre (*args) ===")
book3 = Book("Python alapok", "Guido van Rossum", "789", year=2020, genre="Programming")
book4 = Book("Clean Code", "Robert Martin", "101", year=2008, genre="Programming")
library.add_multiple_books(book3, book4)

print("\n=== Könyv keresése műfaj szerint (**kwargs) ===")
programming_books = library.find_book(genre="Programming")
print("Programozás könyvek:")
for book in programming_books:
    print(f"  - {book}")

print("\n=== Könyv keresése szerző szerint (**kwargs) ===")
orwell_books = library.find_book(author="George Orwell")
print("George Orwell könyvek:")
for book in orwell_books:
    print(f"  - {book}")

print("\n=== Kikölcsönzés (dekorátorral logolja) ===")
library.borrow_book("123")

print("\n=== Statisztika ===")
stats = library.get_stats()
print(f"Összes: {stats['total']}")
print(f"Elérhető: {stats['available']}")
print(f"Kikölcsönözve: {stats['borrowed']}")

print("\n=== Visszahozás (dekorátorral logolja) ===")
book1.return_book()

print("\n=== Elérhető könyvek ===")
for book in library.list_available_books():
    print(f"  - {book}")