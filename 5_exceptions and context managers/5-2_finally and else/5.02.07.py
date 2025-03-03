def get_loss(w1, w2, w3, w4):
    try:
        y = 10 * w1 // w2 - 5 * w2 * w3 + w4
    except ZeroDivisionError:
        return 'деление на ноль'

    else:
        s = w1 // w2
        y = 10 * s - 5 * w2 * w3 + w4

    return y


print(get_loss(2, 0, 3, 4))
