import sys


def input_int_numbers(data_in):
    try:
        data_out = [int(data) for data in data_in.split()]
    except:
        raise TypeError('все числа должны быть целыми')

    return list(data_out)


for line in sys.stdin:
    try:
        res = input_int_numbers(line.strip())
    except:
        continue

    else:
        break

print(res)
