# считывание строки и разбиение ее по пробелам
lst_in = input().split()

lst_out = []

for lst in lst_in:
    try:
        lst_out.append(int(lst))
    except ValueError:
        try:
            lst_out.append(float(lst))
        except ValueError:
            lst_out.append(lst)

print(lst_out)