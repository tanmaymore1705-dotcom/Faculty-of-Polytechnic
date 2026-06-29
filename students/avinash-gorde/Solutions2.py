s = set('abcdefghijklmnopqrstuvwxyz')
vowels = {'a', 'e', 'i', 'o', 'u'}
v = len(s & vowels)
c = len(s - vowels)
print(f"Vowels: {v}")
print(f"Consonants: {c}")
