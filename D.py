def soluton(n):
    h = (n // 60) % 24
    m = str(n % 60)
    print(h,m.zfill(2))


# soluton(240)
#4 00
