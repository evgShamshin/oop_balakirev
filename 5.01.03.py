def get_number(x):
    try:
        return int(x)
    except:
        try:
            return float(x)
        except:
            return x

print(get_number('-3'))
print(get_number('-3.0'))
print(get_number(True))