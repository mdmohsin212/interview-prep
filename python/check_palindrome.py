text = input()

# option 1
print(text == text[::-1])

# option 2
print(text == ''.join(reversed(text)))

# option 3 (Case insensitive)
t = text.replace(" ", "").lower()
print(t == t[::-1])