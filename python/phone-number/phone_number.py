import re


class Phone(object):
    def __init__(self, number):
        self.phoneNumber = number
        self.number = self.checkIfNumCorrect()
        self.area_code = self.getAreaCode()

    def checkIfNumCorrect(self):
        self.phoneNumber = [int(i) for i in list(re.sub("[^0-9]", '', self.phoneNumber))]

        if len(self.phoneNumber) == 11:
            if self.phoneNumber[0] == 1 and self.phoneNumber[1] >= 2 and self.phoneNumber[4] >= 2:
                PhoneNumber = self.phoneNumber[1:]
                correctNumber = ''.join(str(number) for number in PhoneNumber)
                return correctNumber
            else:
                raise ValueError("Not a valid phone number")

        if len(self.phoneNumber) >= 12 or len(self.phoneNumber) < 10:
            raise ValueError("Not a valid phone number")

        if len(self.phoneNumber) == 10:
            if self.phoneNumber[0] >= 2 and self.phoneNumber[3] >= 2:
                self.number = ''.join(str(number) for number in self.phoneNumber)
                correctNumber = ''.join(str(number) for number in self.phoneNumber)
                self.area_code = correctNumber[0:3]
                return correctNumber
            else:
                raise ValueError("Not a valid phone number")

    def getAreaCode(self):
        if len(self.number) == 11:
            return ''.join(self.number[1:4])
        if len(self.number) == 10:
            print(self.number)
            return ''.join(self.number[0:3])

    def pretty(self):
        if len(self.number) == 11:
            self.number = [number for number in self.number[1:]]
            return "(" + self.number[0:3] + ") " + self.number[3:6] + "-" + self.number[6:]
        if len(self.number) == 10:
            return "(" + self.number[0:3] + ") " + self.number[3:6] + "-" + self.number[6:]