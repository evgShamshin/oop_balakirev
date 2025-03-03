val_in = input().split()

try:
    val_out = list(map(int, val_in))
    print(sum(val_out))
except ValueError:
    try:
        val_out = list(map(float, val_in))
        print(sum(val_out))
    except ValueError:
        val_out = val_in
        print(val_out[0] + val_out[1])
