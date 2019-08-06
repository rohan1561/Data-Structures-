def infix_to_postfix2(infixexpr):
     prec = {}
     prec["*"] = 3
     prec["/"] = 3
     prec["+"] = 2
     prec["-"] = 2
     prec["("] = 1
     opStack = Stack()
     postfixList = []
     tokenList = infixexpr.split()
     for token in tokenList:
         if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
             postfixList.append(token)
         elif token == '(':
             opStack.push(token)
         elif token == ')':
             topToken = opStack.pop()
             while topToken != '(':
                 postfixList.append(topToken)
                 topToken = opStack.pop()
