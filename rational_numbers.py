import re

def calc(exppression):
    pattern = '\s+'
    exp = re.split(pattern, exppression)
    op_list = []
    fin_list = []
    for i in range(len(exp)):
        if exp[i] == '*' or\
            exp[i] == '/' or\
            exp[i] == '+' or\
            exp[i] == '-':
            op_list.append(exp[i])

    for i in range(len(exp)):
        if exp[i] != '*' and\
            exp[i] != '/' and\
            exp[i] != '+' and\
            exp[i] != '-':
            fin_list.append(int(exp[i]))

    for i in range(len(op_list)):
        if '*' in op_list :
            index = op_list.index('*')
            fin_list[index] *= fin_list[index + 1]
            del fin_list[index+1]
            del op_list[index]  
        if '/' in op_list:
            index = op_list.index('/')
            fin_list[index] /= fin_list[index + 1]
            del fin_list[index+1]
            del op_list[index]
        if '+' in op_list:
            index = op_list.index('+')
            fin_list[index] += fin_list[index + 1]
            del fin_list[index+1]
            del op_list[index]
        if '-' in op_list:
            index = op_list.index('-')
            fin_list[index] -= fin_list[index + 1]
            del fin_list[index+1]
            del op_list[index]

    return fin_list[0]