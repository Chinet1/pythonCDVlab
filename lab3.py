# ZAD 4

def avg(*args):
    argsSum = 0

    for value in args:
        argsSum += value

    return argsSum / len(args)


print(avg(2, 4, 5, 2, 5))
