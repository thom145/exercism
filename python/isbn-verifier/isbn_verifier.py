def verify(isbn):
    """
    :param isbn: isbn number to check
    :return: whether or not the isbn number is valid or not
    """
    #remove the special char and create a list of all numbers
    all_values = [value for values in list(isbn.split('-')) for value in values]

    if len(all_values) != 10:
        return False

    if all_values[-1] == 'X':
        all_values[-1] = 10

    # check if the values in the list are all integers
    try:
        clean_list = [int(value) for value in all_values]
    except ValueError:
        return False

    # check if the sum of all values mod 11 == 0
    calculated = []
    for value in range(10, 0, -1):
        calculated.append(clean_list[-value] * value)
    if sum(calculated) % 11 == 0:
        return True
    else:
        return False
