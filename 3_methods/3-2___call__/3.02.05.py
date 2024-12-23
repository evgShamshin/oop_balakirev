class DigitRetrieve:
    def __call__(self, digit):
        try:
            return int(digit)
        except ValueError:
            return None


dg = DigitRetrieve()
d1 = dg("1.23")
print(d1)

st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))  # [123, None, None, 0, -5]
print(digits)
