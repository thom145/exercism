def is_armstrong(number):
    """
    Check if a given number is an Amstrong number
    return either true or false
    """
    # create a list of the given number
    number = str(number)
    # get the amount of number
    total_length = len(str(number))
    # calculate
    total_number = [int(i)**total_length for i in number]
    # check if calculation equals given number
    return sum(total_number) == int(number)
