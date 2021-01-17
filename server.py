def addNumbers(x, y):
    return int(x) + int(y)


def multiplyTwoNumbers(x, y):
    c = int(x) * int(y)
    return c


if __name__ == "__main__":
    a = input("enter a number: ")
    b = input("enter a second number: ")
    c = addNumbers(a, b)
    print(c)
    c = multiplyTwoNumbers(a, b)
    print(c)
