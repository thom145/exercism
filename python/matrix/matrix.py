class Matrix(object):

    def __init__(self, matrix_string):
        self.matrix_string = matrix_string.split("\n")

    def column(self, index):
        index -= 1 # index of row starts at 1

        return [int(list_of_numbers.split()[index]) for list_of_numbers in self.matrix_string]

    def row(self, index):
        index -= 1 # index of column starts at 1

        return_list = [int(i) for i in self.matrix_string[index].split(' ')]
        return return_list
