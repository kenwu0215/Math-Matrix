from Matrix import Matrix

if __name__ == "__main__":
    A = Matrix([[1,3],[2,4]])
    B = Matrix([[1],[1]])

    x = A * B

    print(x)