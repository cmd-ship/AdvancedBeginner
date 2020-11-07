import re


def add(a1, a2):
    return a1 + a2


def sub(s1, s2):
    return s1 - s2


def mult(m1, m2):
    return m1 * m2


def div(d1, d2):
    return


def perform_math():
    global run
    global previous

    equation = ""
    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))

    if equation == 'quit':
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]','',equation)
        
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous)+ equation)

        print(previous)

print("Our Magical Calculator")
print("Type quit to exit\n")

run = True
previous = 0

while run:
    perform_math()