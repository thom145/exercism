def raindrops(number):
    returnString = []
    numberDict = {3: 'Pling', 5: 'Plang', 7: 'Plong'}

    for key in sorted(numberDict.keys()):
        if number % key == 0:
            returnString.append(numberDict[key])

    if not returnString:
        return str(number)
    else:
        return ''.join(returnString)
