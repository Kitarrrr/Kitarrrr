f_num = int(input("Введите первое число"))
oper = input("Введите операцию")
s_num = int(input("Введите число"))
dalee = 'c'
while dalee == 'c':
    if oper == '+':
        print(f_num + s_num)
    elif oper == '-':
        print(f_num - s_num)
    elif oper == '*':
        print(f_num * s_num)
    elif oper == '/':
        print(f_num / s_num)
    else:
        print("Error")
    dalee = input("Введите 'c', чтобы продолжить, или любую клавишу, чтобы завершить")
