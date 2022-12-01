import re
def init(exp):
    exp = input('Введите выражение так, что справа и слева от операций был пробел: ')

    pattern = '\s+'
    exp_list = re.split(pattern, exp)
    