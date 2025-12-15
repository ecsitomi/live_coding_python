'''Feladat 1: Leggyakoribb N elem
Írj egy függvényt, amely egy listából visszaadja a TOP N leggyakrabban előforduló elemet.
Ha több elem is ugyanannyiszor fordul elő, bármelyiket visszaadhatod.
Példa: [1, 1, 1, 2, 2, 3], N=2 -> [1, 2]'''

def top_n_frequent(lst, n):
    # Megszámoljuk az előfordulásokat
    count = {}
    for item in lst:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1

    # Rendezzük gyakoriság szerint csökkenő sorrendbe
    sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)

    # Visszaadjuk az első N elemet
    result = []
    for i in range(min(n, len(sorted_items))):
        result.append(sorted_items[i][0])

    return result

print(top_n_frequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
print(top_n_frequent([4, 4, 4, 5, 5, 6, 6, 6, 7], 3))  # [4, 6, 5] vagy [6, 4, 5]
print(top_n_frequent(['a', 'a', 'b', 'b', 'c'], 1))  # ['a'] vagy ['b']

'''Feladat 2: Permutációk generálása
Írj egy függvényt, amely generálja egy string vagy lista összes permutációját.
Permutáció: az elemek összes lehetséges sorrendje.
Példa: "abc" -> ["abc", "acb", "bac", "bca", "cab", "cba"]'''

def generate_permutations(items):
    # Alapeset: ha üres vagy 1 elemű
    if len(items) <= 1:
        return [items]

    permutations = []

    # Végigmegyünk minden elemen
    for i in range(len(items)):
        # Kivesszük az aktuális elemet
        current = items[i]
        # A maradék elemek
        remaining = items[:i] + items[i+1:]

        # Rekurzívan generáljuk a maradék elemek permutációit
        for perm in generate_permutations(remaining):
            permutations.append(current + perm)

    return permutations

def generate_permutations_list(lst):
    if len(lst) <= 1:
        return [lst]

    permutations = []

    for i in range(len(lst)):
        current = lst[i]
        remaining = lst[:i] + lst[i+1:]

        for perm in generate_permutations_list(remaining):
            permutations.append([current] + perm)

    return permutations

print(generate_permutations("abc"))
# ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
print(generate_permutations_list([1, 2, 3]))
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

'''Feladat 3: Email validáció
Írj egy függvényt, amely regex használatával ellenőrzi, hogy egy string érvényes email cím-e.
Alapvető szabályok:
- Van @ karakter
- @ előtt legalább 1 karakter
- @ után van domain név
- Van TLD (top-level domain) pl. .com, .hu
Példa: "test@example.com" -> True, "invalid.email" -> False'''

import re

def is_valid_email(email):
    # Regex minta email validációhoz
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(pattern, email):
        return True
    else:
        return False

def is_valid_email_részletes(email):
    # Részletesebb verzió magyarázattal
    pattern = r'''
        ^                      # String eleje
        [a-zA-Z0-9._%+-]+      # Felhasználónév: betűk, számok, pontok, stb.
        @                      # @ karakter
        [a-zA-Z0-9.-]+         # Domain név
        \.                     # Pont a TLD előtt
        [a-zA-Z]{2,}           # TLD legalább 2 betű
        $                      # String vége
    '''

    return bool(re.match(pattern, email, re.VERBOSE))

print(is_valid_email("test@example.com"))      # True
print(is_valid_email("user.name@domain.co.uk")) # True
print(is_valid_email("invalid.email"))         # False
print(is_valid_email("@example.com"))          # False
print(is_valid_email("test@.com"))             # False
print(is_valid_email("test@example"))          # False

'''Feladat 4: URL Parser
Írj egy függvényt, amely egy URL-t részekre bont:
- Protokoll (http, https, ftp, stb.)
- Domain
- Port (ha van)
- Path (útvonal)
- Query paraméterek
- Fragment (#)
Példa: "https://example.com:8080/path/to/page?name=value&foo=bar#section"'''

def parse_url(url):
    result = {
        'protocol': None,
        'domain': None,
        'port': None,
        'path': None,
        'query': {},
        'fragment': None
    }

    # Protocol
    if '://' in url:
        result['protocol'], url = url.split('://', 1)

    # Fragment
    if '#' in url:
        url, result['fragment'] = url.split('#', 1)

    # Query paraméterek
    if '?' in url:
        url, query_string = url.split('?', 1)
        # Query paraméterek feldolgozása
        for param in query_string.split('&'):
            if '=' in param:
                key, value = param.split('=', 1)
                result['query'][key] = value

    # Path elválasztása a domain-től
    if '/' in url:
        domain_part, result['path'] = url.split('/', 1)
        result['path'] = '/' + result['path']
    else:
        domain_part = url
        result['path'] = '/'

    # Port elválasztása
    if ':' in domain_part:
        result['domain'], port = domain_part.split(':', 1)
        result['port'] = int(port)
    else:
        result['domain'] = domain_part

    return result

url1 = "https://example.com:8080/path/to/page?name=value&foo=bar#section"
print(parse_url(url1))
# {'protocol': 'https', 'domain': 'example.com', 'port': 8080,
#  'path': '/path/to/page', 'query': {'name': 'value', 'foo': 'bar'}, 'fragment': 'section'}

url2 = "http://google.com/search?q=python"
print(parse_url(url2))
# {'protocol': 'http', 'domain': 'google.com', 'port': None,
#  'path': '/search', 'query': {'q': 'python'}, 'fragment': None}

'''Feladat 5: JSON Flattening
Írj egy függvényt, amely egy beágyazott (nested) JSON objektumot egyszerűsít
lapos struktúrává, ahol a kulcsok pontokkal vannak elválasztva.
Példa: {"a": {"b": {"c": 1}}} -> {"a.b.c": 1}'''

def flatten_json(data, parent_key='', separator='.'):
    items = []

    if isinstance(data, dict):
        for key, value in data.items():
            new_key = f"{parent_key}{separator}{key}" if parent_key else key

            if isinstance(value, dict):
                # Rekurzívan flatten-eljük a nested dict-et
                items.extend(flatten_json(value, new_key, separator).items())
            elif isinstance(value, list):
                # Lista kezelése
                for i, item in enumerate(value):
                    list_key = f"{new_key}[{i}]"
                    if isinstance(item, (dict, list)):
                        items.extend(flatten_json(item, list_key, separator).items())
                    else:
                        items.append((list_key, item))
            else:
                items.append((new_key, value))

    return dict(items)

nested = {
    "a": {
        "b": {
            "c": 1,
            "d": 2
        },
        "e": 3
    },
    "f": 4
}
print(flatten_json(nested))
# {'a.b.c': 1, 'a.b.d': 2, 'a.e': 3, 'f': 4}

nested_with_list = {
    "user": {
        "name": "John",
        "hobbies": ["reading", "coding"]
    }
}
print(flatten_json(nested_with_list))
# {'user.name': 'John', 'user.hobbies[0]': 'reading', 'user.hobbies[1]': 'coding'}

'''Feladat 6: Dekorátor írása
Írj dekorátorokat, amelyek:
1. Időmérő - megméri egy függvény futási idejét
2. Memoization - cache-eli a függvény eredményeit (gyorsítja a rekurzív függvényeket)
3. Hívásszámláló - megszámolja, hányszor hívták meg a függvényt'''

import time
from functools import wraps

# 1. Időmérő dekorátor
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} futási ideje: {end_time - start_time:.6f} másodperc")
        return result
    return wrapper

# 2. Memoization dekorátor
def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"Cache találat: {args}")
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

# 3. Hívásszámláló dekorátor
def call_counter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"{func.__name__} meghívva {wrapper.calls}. alkalommal")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

# Példák használatra
@timer
def slow_function():
    time.sleep(1)
    return "Kész"

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

@call_counter
def greet(name):
    return f"Hello, {name}!"

print(slow_function())
print(fibonacci(10))
print(fibonacci(10))  # Gyorsabb lesz, mert cache-ből jön
print(greet("Alice"))
print(greet("Bob"))

'''Feladat 7: Context Manager
Írj egy saját context manager osztályt, amely a 'with' statement-tel használható.
Példa: Fájl megnyitás/bezárás, vagy egyéni erőforrás kezelés.'''

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f"Fájl megnyitása: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Fájl bezárása: {self.filename}")
        if self.file:
            self.file.close()
        # Ha exc_type nem None, akkor kivétel történt
        if exc_type is not None:
            print(f"Hiba történt: {exc_type}, {exc_value}")
        return False  # False = a kivétel továbbadódik, True = elnyeljük

# Használat
# with FileManager('test.txt', 'w') as f:
#     f.write('Hello, World!')

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end = time.time()
        self.elapsed = self.end - self.start
        print(f"Eltelt idő: {self.elapsed:.4f} másodperc")
        return False

# Használat
with Timer():
    time.sleep(0.5)
    print("Művelet végrehajtása...")

# Alternatív módszer: contextlib használata
from contextlib import contextmanager

@contextmanager
def simple_timer():
    start = time.time()
    print("Timer indítása...")
    yield
    end = time.time()
    print(f"Timer vége. Eltelt idő: {end - start:.4f} másodperc")

with simple_timer():
    time.sleep(0.3)
    print("Feladat futása...")
