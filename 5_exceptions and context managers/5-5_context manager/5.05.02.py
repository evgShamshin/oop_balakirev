class Test:
    def __init__(self):
        self.data = 'data'

    def __enter__(self):
        return self.data

    # def __exit__(self, exc_type, exc_val, exc_tb):
        # print(f'exc_type - {exc_type}', f'exc_val - {exc_val}', f'exc_tb - {exc_tb}', sep = '\n')


try:
    with Test() as t:
        res = t + 1

except:
    print()
    print('Ошибка')
