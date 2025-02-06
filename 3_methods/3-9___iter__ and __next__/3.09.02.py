r = range(1, 3000)
res1 = 2022 in r   # res1 = True
res2 = 2022 in r   # res2 = True

r = iter(range(1, 3000))
res1 = 2022 in r   # res1 = True
res2 = 2022 in r   # res1 = False
res3 = 2023 in r