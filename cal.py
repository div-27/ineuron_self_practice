def cal_op(a,b,c):
    if c == "+":
        d = a+b
    elif c == "-":
        d = a-b
    elif c == "*":
        d = a*b
    elif c == "/":
        d = a/b
    else:
        d = "Try again"
    
    return d


def cal():
    a = int(input("First no: "))
    b = int(input("second no: "))
    c = input("operation to be done: ")
    d = cal(a,b,c)


    print(d)

    return d