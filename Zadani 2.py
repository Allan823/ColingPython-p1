from collections import Counter

a = Counter('absdabsdabsd')

keys = list(a.keys())
new_str=""
for i in keys:
    for j in range(a[i]):
        new_str+=i
     
print(new_str)
