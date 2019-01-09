def is_leap_year(year):
    """
    Return if a given year is a leap year
    returns either true or false
    """
    # check if year is evenly divisible by 4
    if year // 4 == year / 4:
        # check if the year is evenly divisible by 100 and not evenly divisible by 400
        if year // 100 == year / 100 and year // 400 != year / 400:
            return False
        else:
            return True
