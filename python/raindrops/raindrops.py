def raindrops(number):
    returnString = []
    numberDict = {3: 'Pling', 5: 'Plang', 7: 'Plong'}

    for key in numberDict.keys():
        if number % key == 0:
            returnString.extend(numberDict[key])

    if not returnString:
        return str(number)
    else:
        return ''.join(returnString)