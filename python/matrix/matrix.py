class Matrix(object):

    def __init__(self, matrix_string):
        try:
            self.matrix_string = [[int(i) for i in list_of_numbers.split(" ")] for list_of_numbers in matrix_string.split("\n")]
        except ValueError:
            return 'Matrix contains a non-integer value'

    def column(self, index):
        index -= 1 # index of row starts at 1
        return [row[index] for row in self.matrix_string]

    def row(self, index):
        index -= 1 # index of column starts at 1
        return self.matrix_string[index]
