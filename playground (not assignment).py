import random
import time
a = ["Bar", "7", "Cherry", "Banana", "Sam"]
b = ["Bar", "7", "Cherry", "Banana", "Sam"]
c = ["Bar", "7", "Cherry", "Banana", "Sam"]
random.shuffle(a)
random.shuffle(b)
random.shuffle(c)
d = a[0]
e = b[0]
f = c[0]
slotmachine = d, e, f
print(slotmachine)
if d == "Bar" and e == "Bar" and f == "Bar":
    print(d)