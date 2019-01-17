from numpy import prod


def largest_product(series, size):
    """
    :param series: string input of all the numbers
    :param size: size of the product
    :return: return the largest product from size
    """
    series = [int(i) for i in list(series)]
    length = len(series)
    largest_number = 0
    for i in range(length-size):
        new_number = prod(series[i:i+size])
        if new_number > largest_number:
            largest_number = new_number
    return largest_number


