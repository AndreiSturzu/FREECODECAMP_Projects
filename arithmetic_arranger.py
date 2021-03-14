tests = [["3 + 855", "3801 - 2", "45 + 43", "123 + 49"], ["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"],
         ["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"],
         ["3 / 855", "3801 - 2", "45 + 43", "123 + 49"], ["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"],
         ["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"], ["32 - 698", "1 - 3801", "45 + 43", "123 + 49"]]


def arithmetic_arranger(*args):
    import operator
    ops = {"+": operator.add, "-": operator.sub}

    problems = args[0]

    calculate = []
    for problem in problems:
        calculate.append((problem.split()[0], problem.split()[2], problem.split()[1]))

    if len(problems) > 5:
        error = "Error: Too many problems."
        print(error)
        return error

    for item in calculate:
        if len(item[0]) > 4:
            error = "Error: Numbers cannot be more than four digits."
            print(error)
            return error

        if len(item[1]) > 4:
            error = "Error: Numbers cannot be more than four digits."
            print(error)
            return error

        for char in item[0]:
            if char not in "0123456789":
                error = "Error: Numbers must only contain digits."
                print(error)
                return error

        for char in item[1]:
            if char not in "0123456789":
                error = "Error: Numbers must only contain digits."
                print(error)
                return error

        if item[2] not in "+-":
            error = "Error: Operator must be '+' or '-'."
            print(error)
            return error

    f, s, t, a = "", "", "", ""
    for operands in calculate:
        lmax = max(len(operands[0]), len(operands[1])) + 2
        if len(operands[0]) > len(operands[1]):
            first = ' ' * (lmax - len(operands[0])) + operands[0]
            second = operands[2] + ' ' * (abs(len(operands[0]) - len(operands[1])) + 1) + operands[1]
        elif len(operands[0]) == len(operands[1]):
            first = ' ' * (lmax - len(operands[0])) + operands[0]
            second = operands[2] + ' ' + operands[1]
        else:
            first = ' ' * (lmax - len(operands[0])) + operands[0]
            second = operands[2] + ' ' + operands[1]
        f += first + '    '
        s += second + '    '
        t += lmax * '-' + '    '
        a += ' ' * (lmax - len(str(ops[operands[2]](int(operands[0]), int(operands[1]))))) + str(ops[operands[2]](int(operands[0]), int(operands[1]))) + "    "

    f = f[0:len(f)-4]
    s = s[0:len(s)-4]
    t = t[0:len(t)-4]
    a = a[0:len(a)-4]


    arranged_problems = f + '\n' + s + '\n' + t

    if True in args:
        arranged_problems += '\n' + a
        print(arranged_problems)
        return arranged_problems
    else:
        print(arranged_problems)
        return arranged_problems + '\n' + a


for p in tests[0:len(tests)-1]:
    arithmetic_arranger(p)
arithmetic_arranger(tests[-1], True)