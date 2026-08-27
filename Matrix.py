from unittest import result

from _testcapi import error
from fractions import Fraction


class Matrix:

    @staticmethod
    def parse_number(x):
        return Fraction(x)

    def __init__(self, data):

        if isinstance(data, str):
            data = [
                [self.parse_number(x) for x in row.split()]
                for row in data.strip().split("\n")
                if row.strip()
            ]

        self.data = data
        self.row = len(data)
        self.column = len(data[0])

    def __repr__(self):
        result = ""

        for row in self.data:
            result += " ".join(map(str, row))
            result += "\n"

        result = result[:-1]
        
        return result

    def __mul__(self, other):

        assert isinstance(other, Matrix), \
            "the variable is not a Matrix"

        assert self.column == other.row, \
            "the number of columns of the former matrix is not equal to the number of rows of the latter one"

        result = []

        for rows in range(self.row):
            row = []

            for col in range(other.column):

                element = 0

                for c in range(self.column):
                    element += (
                        self.data[rows][c]
                        * other.data[c][col]
                    )

                row.append(element)

            result.append(row)

        return Matrix(result)

    def det(self):

        assert self.column == self.row, \
            "Determinant requires a square matrix."

        matrix = [row[:] for row in self.data]

        n = self.row
        result = Fraction(1)

        for col in range(n):

            # 找 pivot
            pivot = col

            for row in range(col, n):
                if abs(matrix[row][col]) > abs(matrix[pivot][col]):
                    pivot = row

            if matrix[pivot][col] == 0:
                return Fraction(0)

            if pivot != col:
                matrix[col], matrix[pivot] = \
                    matrix[pivot], matrix[col]

                result *= -1

            pivot_value = matrix[col][col]

            result *= pivot_value

            for row in range(col + 1, n):

                factor = matrix[row][col] / pivot_value

                for k in range(col, n):
                    matrix[row][k] -= \
                        factor * matrix[col][k]

        return result
    
    def inverse(self):
        assert self.row == self.column, \
        "Inverse requires a square matrix."

        n = self.row

        matrix = [
            self.data[i][:] +
            [Fraction(int(i == j)) for j in range(n)]
            for i in range(n)
        ]

        for col in range(n):

            pivot = col

            for row in range(col, n):
                if abs(matrix[row][col]) > abs(matrix[pivot][col]):
                    pivot = row

            if matrix[pivot][col] == 0:
                raise ValueError("Matrix is not invertible.")

            if pivot != col:
                matrix[col], matrix[pivot] = \
                    matrix[pivot], matrix[col]

            pivot_value = matrix[col][col]

            for j in range(2 * n):
                matrix[col][j] /= pivot_value

            for row in range(n):

                if row == col:
                    continue

                factor = matrix[row][col]

                for j in range(2 * n):
                    matrix[row][j] -= \
                        factor * matrix[col][j]

        result = [
            row[n:]
            for row in matrix
        ]

        return Matrix(result)

    def __add__(self, other):

        assert self.row == other.row and self.column == other.column\
            , "Matrix syntax error"

        result = []

        for r in range(self.row):
            row = []
            for c in range(self.column):
                row.append(self.data[r][c] + other.data[r][c])
            result.append(row)

        return Matrix(result)

    def __sub__(self, other):

        assert self.row == other.row and self.column == other.column,\
            "Matrix syntax error"

        result = []

        for r in range(self.row):
            row = []
            for c in range(self.column):
                row.append(self.data[r][c] - other.data[r][c])
            result.append(row)

        return Matrix(result)
