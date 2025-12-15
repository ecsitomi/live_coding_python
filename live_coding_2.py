'''Feladat 1: FizzBuzz
Írj egy függvényt, amely 1-től n-ig kiírja a számokat, de:
- 3 többszöröseire "Fizz"-t ír
- 5 többszöröseire "Buzz"-t ír
- Mindkettő többszöröseire "FizzBuzz"-t ír
Példa: n=15 -> [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]'''

def fizzbuzz(n):
    result = []

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)

    return result

print(fizzbuzz(15))
# [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']

'''Feladat 2: Prímszám ellenőrzés
Írj egy függvényt, amely ellenőrzi, hogy egy szám prímszám-e vagy sem.
Prímszám: csak 1-gyel és önmagával osztható pozitív egész szám (nagyobb mint 1).
Példa: is_prime(7) -> True, is_prime(10) -> False'''

def is_prime(n):
    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True

print(is_prime(7))   # True
print(is_prime(10))  # False
print(is_prime(2))   # True
print(is_prime(1))   # False
print(is_prime(17))  # True

'''Feladat 3: Faktoriális számítás
Írj két függvényt a faktoriális kiszámítására:
- Iteratív megoldás (ciklussal)
- Rekurzív megoldás (önmagát hívja)
Példa: 5! = 5 * 4 * 3 * 2 * 1 = 120'''

def factorial_iterative(n):
    if n < 0:
        return None

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result

def factorial_recursive(n):
    if n < 0:
        return None

    if n == 0 or n == 1:
        return 1

    return n * factorial_recursive(n - 1)

print(factorial_iterative(5))  # 120
print(factorial_recursive(5))  # 120
print(factorial_iterative(0))  # 1
print(factorial_recursive(6))  # 720

'''Feladat 4: Lista összegzés és átlag számítás
Írj függvényeket, amelyek:
- Kiszámítják egy számokat tartalmazó lista összegét
- Kiszámítják egy számokat tartalmazó lista átlagát
Példa: [1, 2, 3, 4, 5] -> összeg: 15, átlag: 3.0'''

def list_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def list_average(numbers):
    if len(numbers) == 0:
        return 0

    return list_sum(numbers) / len(numbers)

print(list_sum([1, 2, 3, 4, 5]))      # 15
print(list_average([1, 2, 3, 4, 5]))  # 3.0
print(list_sum([10, 20, 30]))         # 60
print(list_average([10, 20, 30]))     # 20.0
print(list_average([]))               # 0

'''Feladat 5: String megfordítás
Írj több függvényt, amelyek különböző módokon fordítanak meg egy stringet:
- Slice használatával (legegyszerűbb)
- Ciklussal és string összefűzéssel
- Lista és reverse metódussal
Példa: "hello" -> "olleh"'''

def reverse_string_slice(s):
    return s[::-1]

def reverse_string_loop(s):
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

def reverse_string_list(s):
    char_list = list(s)
    char_list.reverse()
    return ''.join(char_list)

print(reverse_string_slice("hello"))    # olleh
print(reverse_string_loop("hello"))     # olleh
print(reverse_string_list("hello"))     # olleh
print(reverse_string_slice("Python"))   # nohtyP
