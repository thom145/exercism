class Phone(object):
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def something(self):
        all_values = [value for values in self.phone_number.split() for value in values]
        all_integers = [int(integer) for integer in all_values if integer.isdigit()]
        return self.check_list(all_integers)

    def check_list(self, list_to_check):
        if list_to_check[0] == 1 and len(list_to_check) > 12:
            return False
        elif list_to_check[0] == 1 and len(list_to_check) == 12 and list_to_check[4] < 2:
            return False
        elif list_to_check[0] > 1 and list_to_check[3] < 2:
            return False
        else:
            return True

print(Phone("1253-wabc-7890").something())
