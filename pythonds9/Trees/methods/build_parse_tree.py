from .. import Stack.Stack.Stack
from pythonds9 import BinaryTree

def BuildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack.Stack()
    eTree = BinaryTree.BinaryTree('')
    pStack.push(eTree)
    current_tree = eTree
    for i in fplist:
        if i == '(':
            current_tree.insert_left('')
            pStack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif i not in ['+', '-', '*', '/', ')']:
            current_tree.set_root_val(int(i))
            parent = pStack.pop()
            current_tree = parent
        elif i in ['+', '-', '*', '/']:
            current_tree.set_root_val(i)
            current_tree.insert_right('')
            pStack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i == ')':
            current_tree = pStack.pop()
        else:
            raise ValueError

    return eTree


def preorder(tree):
    if tree:
        print(tree.get_root_val())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())

def postorder(tree):
    if tree != None:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.get_root_val())

def evaluate(parse_tree):
    opers = {'+': operator.add,
             '-': operator.sub,
             '*': operator.mul,
             '/': operator.truediv}
    left = parse_tree.get_left_child()
    right = parse_tree.get_right_child()

    if left and right:
        return opers[parse_tree.get_root_val()](evaluate(left),\
                evaluate(right))

    else:
        return parse_tree.get_root_val()


def evaluate_post(tree):
    opers = {'+': operator.add,
             '-': operator.sub,
             '*': operator.mul,
             '/': operator.truediv}

    res1 = None
    res2 = None
    if tree:
        res1 = evaluate_post(tree.get_left_child())
        res2 = evaluate_post(tree.get_right_child())
        if res1 and res2:
            return opers[tree.get_root_val()](res1, res2)

        else: return tree.get_root_val()

def inorder(tree):
    if tree:
        inorder(tree.get_left_child())
        print(tree.get_root_val())
        inorder(tree.get_right_child())

def printexp(tree):
    sVal = ''
    if tree:
        left_child = tree.get_left_child()
        right_child = tree.get_right_child()
        if left_child and right_child:
            sVal = '(' + printexp(left_child)
            sVal = sVal + str(tree.get_root_val())
            sVal = sVal + printexp(right_child) + ')'
        else:
            sVal = str(tree.get_root_val())

    return sVal


if __name__ == '__main__':
    expr = '( ( 10 + 5 ) * 3 )'
    print(expr)
    pt = BuildParseTree('( ( 10 + 5 ) * 3 )')
    preorder(pt)
    print('xxxxxxxxxxxx')
    postorder(pt)
    print('xxxxxxxxxxxx')
    inorder(pt)
    print('xxxxxxxxxxxx')
    print(printexp(pt))

