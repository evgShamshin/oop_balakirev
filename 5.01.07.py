# считывание строки и разбиение ее по пробелам
lst_in = input().split()
res = 0

for l in lst_in:
    try:
        res += int(l)
    except ValueError:
        continue
print(res)