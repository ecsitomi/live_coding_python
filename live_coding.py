'''Feladat 1: Palindróma ellenőrzés
Írj egy Python függvényt, amely egyetlen s string paramétert fogad, és True értékkel tér vissza, ha a string palindróma (mindkét irányból megegyező), egyébként False. A kis- és nagybetűk, valamint a szóközök nem számítanak.
Példa: "A man, a plan, a canal: Panama" -> True'''

def is_palindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

def is_palindrome_hosszabb(s):
    # 1. Tisztítás: csak betűk és számok maradnak, kisbetűsítve
    cleaned = ''
    for char in s:
        if char.isalnum():
            cleaned += char.lower()
    
    # 2. Ellenőrzés: ugyanaz-e mindkét irányból
    reversed_cleaned = cleaned[::-1]
    
    if cleaned == reversed_cleaned:
        return True
    else:
        return False
    
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))  # False

'''Feladat 2: Duplikátumok eltávolítása listából
Írj egy függvényt, amely egy listát fogad, és egy új listát ad vissza, amely az eredeti lista összes egyedi elemét tartalmazza, az eredeti sorrendben.
Példa: [1, 2, 2, 3, 1, 4] -> [1, 2, 3, 4]
'''

def remove_duplicates(lst):
    unique_list = []
    
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    
    return unique_list

print(remove_duplicates([1, 2, 2, 3, 1, 4]))  # [1, 2, 3, 4]
print(remove_duplicates(['a', 'b', 'a', 'c']))  # ['a', 'b', 'c']

'''Feladat 3: Karakterek számolása
Írj egy függvényt, amely megszámolja egy adott stringben az egyes karakterek előfordulását, és visszaad egy szótárat, ahol a kulcsok a karakterek, az értékek pedig az előfordulások száma.
Példa: "hello world" -> {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}'''

def count_characters(s):
    char_count = {}
    
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count

print(count_characters("hello world"))
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
print(count_characters("aaa"))
# {'a': 3}

'''Feladat 4: Fibonacci sorozat
Írj egy függvényt, amely a Fibonacci sorozat első N elemét generálja és listaként adja vissza. A sorozat úgy kezdődik, hogy 0, 1, a következő elemek pedig az előző kettő összege.
Példa: N=5 -> [0, 1, 1, 2, 3]'''

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_list = [0, 1]
    
    for i in range(2, n):
        next_number = fib_list[i-1] + fib_list[i-2]
        fib_list.append(next_number)
    
    return fib_list

print(fibonacci(2))  # [0, 1]
print(fibonacci(5))  # [0, 1, 1, 2, 3]

'''Feladat 5: Anagramma ellenőrzés
Írj egy függvényt, amely két stringet fogad, és True értékkel tér vissza, ha a két szó vagy kifejezés anagramma (ugyanazokból a betűkből áll, csak más sorrendben), egyébként False.
Példa: "listen", "silent" -> True'''

def are_anagrams(s1, s2):
    cleaned_s1 = ''.join(sorted(char.lower() for char in s1 if char.isalnum()))
    cleaned_s2 = ''.join(sorted(char.lower() for char in s2 if char.isalnum()))
    
    return cleaned_s1 == cleaned_s2

def is_anagram_hosszabb(s1, s2):
    cleaned_s1 = s1.replace(' ', '').lower()
    cleaned_s2 = s2.replace(' ', '').lower()
    
    if len(cleaned_s1) != len(cleaned_s2):
        return False
    
    sorted_s1 = sorted(cleaned_s1)
    sorted_s2 = sorted(cleaned_s2)
    
    if sorted_s1 == sorted_s2:
        return True
    else:
        return False

print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))    # False

'''Feladat 6: Két szám összege (Two Sum probléma)
Adott egy egész számokból álló lista (nums) és egy célösszeg (target). Keress két különböző számot a listában, amelyek összege megegyezik a célösszeggel, és add vissza az indexeiket egy listában. Feltételezheted, hogy pontosan egy megoldás létezik.
Példa: nums = [2, 7, 11, 15], target = 9 -> [0, 1] (mivel nums[0] + nums[1] == 9)'''

def two_sum(nums, target): #O(n) megoldás
    num_indices = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            return [num_indices[complement], index]
        num_indices[num] = index
    return []

def two_sum(nums, target): #O(n^2) megoldás
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    
    return []

print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
print(two_sum([3, 2, 4], 6))       # [1, 2]

'''Feladat 7: Bináris keresés implementálása
Írj egy függvényt, amely egy rendezett listában és egy célszámban keresi meg a célszám indexét bináris keresési algoritmussal. Ha a szám nem található, térjen vissza -1-gyel. Az algoritmus időkomplexitása O(log N) legyen.'''

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

print(binary_search([1, 2, 3, 4, 5], 3)) #2

'''Feladat 8: Zárójelek érvényessége
Írj egy függvényt, amely egy stringet fogad, amely csak a következő karaktereket tartalmazza: '(', ')', '{', '}', '[', ']'. A függvénynek True értékkel kell visszatérnie, ha a bemeneti string érvényes (a zárójelek helyesen vannak párosítva és sorrendben), egyébként False.'''

def is_valid_parentheses(s):
    stack = []
    pairs = {'(': ')', '{': '}', '[': ']'}
    
    for char in s:
        if char in pairs:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            last_open = stack.pop()
            if pairs[last_open] != char:
                return False
    
    if len(stack) == 0:
        return True
    else:
        return False
    
'''Feladat 9: Maximum szubrész összeg
Írj egy függvényt, amely egy egész számokat tartalmazó listát fogad, és visszaadja a legnagyobb összegű szubrész összegét (a szubrész legalább egy elemet tartalmaz).
Példa: [-2,1,-3,4,-1,2,1,-5,4] -> 6 (a szubrész [4,-1,2,1] összege 6)'''

def max_subarray_sum(nums):
    max_current = max_global = nums[0]
    
    for i in range(1, len(nums)):
        max_current = max(nums[i], max_current + nums[i])
        if max_current > max_global:
            max_global = max_current
    
    return max_global

print(max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))  #6
print(max_subarray_sum([1]))  #1    

'''Feladat 10: Leggyakoribb elem
Írj egy függvényt, amely egy listát fogad, és visszaadja a leggyakrabban előforduló elemet. Ha több elem is ugyanannyiszor fordul elő, bármelyiküket visszaadhatod.
Példa: [1, 2, 3, 2, 4, 2, 5] -> 2'''

def most_frequent_element(lst):
    count = {}
    for item in lst:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1 
    max_count = 0
    most_frequent = None    
    for item, freq in count.items():
        if freq > max_count:
            max_count = freq
            most_frequent = item
    return most_frequent

        
