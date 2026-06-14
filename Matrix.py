class Matrix:
    def __init__(self, data):
        self.data = data

        self.row = len(data)
        self.column = len(data[0])


    def __repr__(self):

        result = ""

        for row in self.data:
            result += " ".join(map(str, row))
            result += "\n"

        return result

    def __mul__(self, other):

        assert isinstance(other, Matrix), "the variable is not a Matrix"

        assert self.column == other.row, "the number of columns of the former matrix is not equal to the number of rows of the latter one"


        result = []
        for rows in range(self.row):
            row = []

            for col in range(other.column):
                element = 0
                for c in range(self.column):
                    element += (self.data[rows][c] ) * (other.data[c][col])
                row.append(element)
            result.append(row)
        return Matrix(result)
