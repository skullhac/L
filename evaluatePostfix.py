from Chapter7.lliststack import Stack
from infix2postfix import infixToPostfix
def evaluatePostfix(e):
    #  Get the length of expression
    size = len(e)
    a = 0
    b = 0
    s = Stack()
    isVaild = True
    i = 0
    #  work with (+,-,/,*,%) operator
    while (i < size and isVaild):
        if (e[i] >= '0'
                and e[i] <= '9'):
            a = ord(e[i]) - ord('0')
            s.push(a)
        elif (len(s) > 1):
            a = s.pop()
            b = s.pop()
            #  Perform arithmetic operations between 2 operands
            if (e[i] == '+'):
                s.push(b + a)
            elif (e[i] == '-'):
                s.push(b - a)
            elif (e[i] == '*'):
                s.push(b * a)
            elif (e[i] == '/'):
                s.push(int(b / a))
            elif (e[i] == '%'):
                s.push(b % a)
            else:
                #  When use other operator
                isVaild = False

        elif (len(s) == 1):
            #  Special case
            #  When use +, - at the beginning
            if (e[i] == '-'):
                a = s.pop()
                s.push(-a)
            elif (e[i] != '+'):
                #  When not use  +,-
                isVaild = False

        else:
            isVaild = False

        i += 1

    if (isVaild == False):
        #  Possible case use other operators
        #  1) When using special operators
        #  2) Or expression is invalid
        print(e, " Invalid expression ")
        return

    print(e, " = ", s.pop())

exp1 = str((1+2)*(3+5))
postexpr1=(infixToPostfix(exp1))
evaluatePostfix(postexpr1)
# evaluatePostfix('12+35+*')
# evaluatePostfix('72*62/+4+-')