from Matrix import Matrix

if __name__ == "__main__":
    A = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    B = Matrix([[10, 11, 12], [13, 14, 15], [16, 17, 18]])

    C = A + B

    print(C)