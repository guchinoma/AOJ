def calc_second_arg(number_1, number_2):
    while number_2 < 10:
        multiple = number_1 * number_2
        print "%dx%d=%d" % (number_1, number_2, multiple)
        number_2 = number_2 + 1

def calc_first_arg():
    a = 1
    b = 1
    while a < 10:
        calc_second_arg(a, b)
        a = a + 1

calc_first_arg()
    
