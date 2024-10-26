class String:
    is_empty = False

s1 = String()
s2 = String()

s2.is_empty = True

print(f"String - {String.__dict__}")
print(f"s1 - {s1.__dict__}")
print(f"s2 - {s2.__dict__}")