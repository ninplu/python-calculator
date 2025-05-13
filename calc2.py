#write a first digit
while True:
    try:
        a = float((input('Write a first number: ')))
        break
    except:
        print('Invalid input')
#calculate for other digits and print
while True:
        oper = input('Choose an operation(+, -, *, / or ^): ')
        if oper not in ('+', '-', '*', '/', '^', 'result', '='):
            print('Invalid input')
            continue
        if oper == 'result' or oper == '=':
            break
        try:
            b = float(input('Choose a second number: '))
        except ValueError:
            print('Invalid input')
            continue
        if oper == '+':
            a = a + b
        elif oper == '-':
            a = a - b
        elif oper == '*':
           a = a * b
        elif oper == '^':
            a = a ** b
        elif oper == '/':
            if b == 0:
                print('Error')
                continue
            a = a / b
print(a)
 