class Matrix(object):
    return_list = []

    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def column(self, index):
        index -= 1 # index of row starts at 1

        for list_of_numbers in self.matrix_string.split("\n"):
            self.return_list.append(int(list_of_numbers.split()[index]))
        return self.return_list

    def row(self, index):
        index -= 1 # index of column starts at 1

        for list_of_numbers in self.matrix_string.split("\n"):
            row = [int(number) for number in list_of_numbers.split()]
            self.return_list.append(row)
        return self.return_list[index]