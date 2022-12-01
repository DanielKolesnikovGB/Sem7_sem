import view
import rational_numbers
import rational_numbers_init
import logger as log
import complex_numbers
import complex_numbers_init

def start ():
    res = input(('Веберите с какими числами будут производиться опрации:\n1. Рациональные\n2. Комплексные\n'))
    if res == '1':
        view.result(rational_numbers.calc(rational_numbers_init.init()))
        exit()
    if res == '2':
        view.result(complex_numbers.com_calc(complex_numbers_init.init_1(), complex_numbers_init.init_2(), complex_numbers_init.init_3()))