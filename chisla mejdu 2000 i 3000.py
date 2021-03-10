res = []
for x in range (2000, 3201):
    if not x % 7 and x % 5:
        res.append(str(x))
 
res = ", ".join(res)
 
print(res)
