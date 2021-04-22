Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================== RESTART: C:/Users/Karaken/Desktop/Ulitka.py =================
>>> f = lambda m:m and m.pop(0)+f([list(x)for x in zip(*m)][::-1])
>>> arr = [[1,2,3],[8,9,4],[7,6,5]]
>>> f(arr)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 