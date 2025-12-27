text = input()

# option 1
print(text[::-1])

# option 2
print(''.join(reversed(text)))

#option 3
rev = ""
for c in text:
    rev = c + rev
print(rev)