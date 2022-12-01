import view
import rational_numbers
import rational_numbers_init
import logger as log

def start ():
    view.result(rational_numbers.calc(rational_numbers_init.init()))
    log.action_notes(rational_numbers_init.init(),\
        rational_numbers.calc(rational_numbers_init.init()))
