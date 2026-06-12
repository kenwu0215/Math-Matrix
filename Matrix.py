class Matrix:
    def __init__(self, data):
        self.data = data

        self.row = len(data)
        self.column = len(data[0])


    def __repr__(self):

        reslut = ""

        for row in self.data:
            reslut += " ".join(map(str, row))
            reslut += "\n"

        return reslut