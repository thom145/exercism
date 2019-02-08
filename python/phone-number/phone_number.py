import re


class Phone(object):
    def __init__(self, phone_number):

        self.phone_number = phone_number

    def something(self):
        s = re.sub(r'[^\w\s]', '', self.phone_number)
        return s

print(Phone("1253-wabc-7890").something())
