from unittest import result

from _testcapi import error


class Matrix:
    def __init__(self, data):
        self.data = data

        self.row = len(data)
        self.column = len(data[0])

        for row in data:
            assert len(row) == self.column, "Matrix syntax error"



    def __repr__(self):

        reslut = ""

        for row in self.data:
            reslut += " ".join(map(str, row))
            reslut += "\n"

        return reslut

    def __add__(self, other):

        assert self.row == other.row and self.column == other.column, "Matrix syntax error"

        result = []

        for r in range(self.row):
            row = []
            for c in range(self.column):
                row.append(self.data[r][c] + other.data[r][c])
            result.append(row)

        return Matrix(result)

    def __sub__(self, other):

        assert self.row == other.row and self.column == other.column, "Matrix syntax error"

        result = []

        for r in range(self.row):
            row = []
            for c in range(self.column):
                row.append(self.data[r][c] - other.data[r][c])
            result.append(row)

        return Matrix(result)
