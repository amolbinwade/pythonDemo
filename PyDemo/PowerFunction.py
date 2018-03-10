

def powerF(num, power):
    sum1 = 1
    for i in range(0, int(power/3)):
        sum1 = sum1 * num
    sum1 = sum1 * sum1 * sum1
    print(str(sum1))


def powerF1(num, power):
    sum1 = 1
    for i in range(0, int(power)):
        sum1 = sum1 * num
    print(str(sum1))

powerF(2, 9)
powerF1(2, 9)
