from datetime import datetime as dt

def action_notes(exp, res):
    time = dt.now().strftime('%H%M')
    with open('log.csv', 'a') as file:
        file.write(time, ' ', exp, ' = ', str(res), '\n')
