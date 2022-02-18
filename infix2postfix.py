from Chapter7.lliststack import Stack

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()
    # print("Token List: ",tokenList)
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
            # print('postfixList: ',postfixList)
        elif token == '(':
            opStack.push(token)
            # print('Taken is (, push into opStack: ', opStack.peek())

        elif token == ')':
            # print('Taken is ), pop opStack: ')
            topToken = opStack.pop()

            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                # print('opStack peek %c >= token %c, put %c in the postfixList : ' %(opStack.peek(),token,opStack.peek()))
                postfixList.append(opStack.pop())
            opStack.push(token)
            # print('token is %c, push into opStack: '%(token))

    while not opStack.isEmpty():
        # print('Stack Peek put into postfixList: ', opStack.peek())
        postfixList.append(opStack.pop())

    return " ".join(postfixList)

# print(infixToPostfix("A * B + C * D"))
# print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
