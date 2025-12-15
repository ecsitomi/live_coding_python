'''Feladat 1: Merge két rendezett lista
Írj egy függvényt, amely két már rendezett listát egyesít egyetlen rendezett listává.
Az algoritmus hatékonyan egyesítse a listákat anélkül, hogy újra rendezné őket.
Példa: [1, 3, 5], [2, 4, 6] -> [1, 2, 3, 4, 5, 6]'''

def merge_sorted_lists(list1, list2):
    merged = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    # Hozzáadjuk a maradék elemeket
    while i < len(list1):
        merged.append(list1[i])
        i += 1

    while j < len(list2):
        merged.append(list2[j])
        j += 1

    return merged

print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6]
print(merge_sorted_lists([1, 2, 3], [4, 5, 6]))  # [1, 2, 3, 4, 5, 6]
print(merge_sorted_lists([1], []))               # [1]
print(merge_sorted_lists([1, 5, 9], [2, 3, 10, 11]))  # [1, 2, 3, 5, 9, 10, 11]

'''Feladat 2: Első nem ismétlődő karakter
Írj egy függvényt, amely egy stringben megtalálja az első olyan karaktert,
amely csak egyszer fordul elő. Ha nincs ilyen, térjen vissza None-nal.
Példa: "leetcode" -> "l", "loveleetcode" -> "v", "aabb" -> None'''

def first_unique_character(s):
    # Megszámoljuk minden karakter előfordulását
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Megkeressük az első karaktert, ami csak egyszer fordul elő
    for char in s:
        if char_count[char] == 1:
            return char

    return None

print(first_unique_character("leetcode"))      # l
print(first_unique_character("loveleetcode"))  # v
print(first_unique_character("aabb"))          # None
print(first_unique_character("z"))             # z
print(first_unique_character(""))              # None

'''Feladat 3: Rotált string ellenőrzés
Írj egy függvényt, amely ellenőrzi, hogy az egyik string a másik rotációja-e.
Rotáció: a string karaktereit körkörösen elforgatjuk.
Példa: "waterbottle" rotációja "erbottlewat" (7 karakterrel jobbra forgatva)
Tipp: ha s2 az s1 rotációja, akkor s2 benne van s1+s1-ben!'''

def is_rotation(s1, s2):
    # Először ellenőrizzük, hogy ugyanolyan hosszúak-e
    if len(s1) != len(s2):
        return False

    # Ha üres stringek
    if len(s1) == 0:
        return True

    # Ha s2 az s1 rotációja, akkor s2 substring-je kell legyen s1+s1-nek
    doubled = s1 + s1
    return s2 in doubled

def is_rotation_hosszabb(s1, s2):
    if len(s1) != len(s2) or len(s1) == 0:
        return False

    # Végigpróbáljuk az összes lehetséges rotációt
    for i in range(len(s1)):
        rotated = s1[i:] + s1[:i]
        if rotated == s2:
            return True

    return False

print(is_rotation("waterbottle", "erbottlewat"))  # True
print(is_rotation("hello", "lohel"))              # True
print(is_rotation("hello", "world"))              # False
print(is_rotation("abc", "bca"))                  # True
print(is_rotation("abc", "cab"))                  # True
print(is_rotation("abc", "acb"))                  # False

'''Feladat 4: Leghosszabb szó adott betűkből
Adott egy szótár (szavak listája) és egy betűkészlet. Keresd meg a leghosszabb szót
a szótárból, amely képezhető a megadott betűkből. Minden betűt csak annyiszor
használhatsz, ahányszor megjelenik a betűkészletben.
Példa: dictionary = ["cat", "cats", "dog", "tiger"], letters = "catstiger" -> "tiger"'''

def longest_word_from_letters(dictionary, letters):
    # Megszámoljuk a rendelkezésre álló betűket
    available_letters = {}
    for char in letters:
        if char in available_letters:
            available_letters[char] += 1
        else:
            available_letters[char] = 1

    longest = ""

    for word in dictionary:
        # Ellenőrizzük, hogy a szó képezhető-e
        word_letters = {}
        for char in word:
            if char in word_letters:
                word_letters[char] += 1
            else:
                word_letters[char] = 1

        # Megnézzük, hogy van-e elég betűnk
        can_form = True
        for char, count in word_letters.items():
            if char not in available_letters or available_letters[char] < count:
                can_form = False
                break

        # Ha képezhető és hosszabb mint az eddigi leghosszabb
        if can_form and len(word) > len(longest):
            longest = word

    return longest if longest else None

dictionary = ["cat", "cats", "dog", "tiger", "elephant"]
print(longest_word_from_letters(dictionary, "catstiger"))  # tiger
print(longest_word_from_letters(dictionary, "catsdgo"))    # cats
print(longest_word_from_letters(dictionary, "xyz"))        # None

'''Feladat 5: Caesar cipher titkosítás és visszafejtés
Írj két függvényt:
1. Titkosít egy szöveget Caesar cipher-rel (minden betűt elcsúsztat n pozícióval)
2. Visszafejti a titkosított szöveget
ROT13 egy speciális eset, ahol n=13.
Példa: "ABC" shift=1 -> "BCD", "XYZ" shift=3 -> "ABC"'''

def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            # Nagybetűk esetén (A=65, Z=90)
            shifted = ((ord(char) - ord('A') + shift) % 26) + ord('A')
            result += chr(shifted)
        elif char.islower():
            # Kisbetűk esetén (a=97, z=122)
            shifted = ((ord(char) - ord('a') + shift) % 26) + ord('a')
            result += chr(shifted)
        else:
            # Nem betű karaktereket változatlanul hagyjuk
            result += char

    return result

def caesar_decrypt(text, shift):
    # Visszafejtéshez csak negatív eltolást használunk
    return caesar_encrypt(text, -shift)

def rot13(text):
    # ROT13 speciális eset: 13 pozíciós eltolás
    return caesar_encrypt(text, 13)

print(caesar_encrypt("ABC", 1))           # BCD
print(caesar_encrypt("XYZ", 3))           # ABC
print(caesar_encrypt("Hello, World!", 5)) # Mjqqt, Btwqi!
print(caesar_decrypt("Mjqqt, Btwqi!", 5)) # Hello, World!
print(rot13("Hello"))                     # Uryyb
print(rot13("Uryyb"))                     # Hello (ROT13 kétszer alkalmazva visszaadja az eredetit)
