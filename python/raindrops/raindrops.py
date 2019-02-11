def raindrops(number):
    list_to_check = [i for i in range(1, number+1) if (number/i).is_integer()]

    num_to_string = []
    for num in list_to_check:
        if num == 3:
            num_to_string.extend('Pling')
        if num == 5:
            num_to_string.extend('Plang')
        if num == 7:
            num_to_string.extend('Plong')

    if num_to_string == []:
        return str(number)
    else:
        return ''.join(num_to_string)
