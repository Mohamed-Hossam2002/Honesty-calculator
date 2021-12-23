memory = 0
while True:
    while True:
        x, oper, y = input('Enter an equation\n').split(' ')
        if x == 'M':
            x = memory
        if y == 'M':
            y = memory
        try:
            if x != 'M':
                x = float(x)
            if y != 'M':
                y = float(y)
        except ValueError:
            print('Do you even know what numbers are? Stay focused!')
            continue

        if oper not in '+-*/':
            print(
                "Yes ... an interesting math operation. You've slept through all classes, haven't you?")
            continue

        def is_one_digit(v):
            if -10 < v < 10 and int(v) == v:
                return True
            return False

        def check(v1, v2, v3):
            msg = ''
            if is_one_digit(v1) and is_one_digit(v2):
                msg += " ... lazy"
            if (v1 == 1 or v2 == 1) and v3 == '*':
                msg += " ... very lazy"
            if (v1 == 0 or v2 == 0) and v3 in '*+-':
                msg += " ... very, very lazy"
            if msg != '':
                msg = "You are" + msg
                print(msg)
        check(x, y, oper)

        if oper == '/' and y == 0:
            print("Yeah... division by zero. Smart move...")
            continue

        break

    operations_dict = {'+': x + y, '-': x - y, '*': x * y}
    for operation, value in operations_dict.items():
        if oper == '/':
            result = float(x / y)
            print(result)
            break
        if operation == oper:
            result = float(value)
            print(result)
            break

    answer = None
    while answer != 'y' and answer != 'n':
        answer = input("Do you want to store the result? (y / n):\n").lower()
        if answer == 'y':
            if is_one_digit(result):
                msg_index = 10
                msg_10 = "Are you sure? It is only one digit! (y / n)"
                msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
                msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

                sub_answer = None
                while sub_answer != 'y' and sub_answer != 'n':
                    sub_answer = input(eval(f'msg_{msg_index}') + '\n').lower()
                    while sub_answer == 'y' and msg_index < 12:
                        msg_index += 1
                        sub_answer = input(eval(f'msg_{msg_index}') + '\n').lower()

                    if msg_index >= 12:
                        memory = result
            else:
                memory = result

    answer_2 = input("Do you want to continue calculations? (y / n):\n").lower()
    while answer_2 != 'y' and answer_2 != 'n':
        answer_2 = input("Do you want to continue calculations? (y / n):\n").lower()

    if answer_2 == 'y':
        continue
    else:
        break
