text = input().lower()

vowels = "aeiou"

# option 1
cnt = 0
for t in text:
    if t in vowels:
        cnt += 1

print(cnt)

# option 2
print(sum(1 for c in text if c in vowels))

# option 3
print(len([c for c in text if c in vowels]))

# option 4
print(len(list(filter(lambda x : x in vowels, text))))