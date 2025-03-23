
def calculator(x,y,o):
    if o not in ["+", "-", "*", "/"]:
        return "Invalid operand"

    if o=='+':
        return x+y
    elif o=='-':
        return x-y
    elif o=='*':
        return x*y
    elif o=='/':
        return x/y

if __name__ == "__main__":
    x=float(input())
    o=input()
    y=float(input())
    result=calculator(x,y,o)
    print(result)