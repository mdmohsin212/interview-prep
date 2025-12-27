s = input()
s1 = input()

# option 1
if len(s) != len(s1):
    print(False)
else:
    if sorted(s) == sorted(s1):
        print(True)
    else:
        print(False)

# option 2
from collections import Counter
print(Counter(s) == Counter(s1))