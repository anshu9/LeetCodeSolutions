def add_digits_simple(num):
    num_total = 0

    while (len(str(num)) > 1):
        num_string = str(num)
        for i in range(len(num_string)):
            num_total = num_total + int(num_string[i])
        num = num_total
        num_total = 0

    return num

def add_digits_digital_root(num):
    """
    This method comes solving the digital root for the number given.
    The formula for solving the digital root is:
    dr = 1 + ((n-1) % 9)
    """
    return 1 + ((num - 1) % 9)
