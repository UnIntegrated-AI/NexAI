class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return str(self.data)
    
    def __add__(self, other):

        if len(self.data) != len(other.data):
            raise ValueError("Matrices must have same number of rows.")
        
        if len(self.data[0]) != len(other.data[0]):
            raise ValueError("Matrices must have same number of columns.")

        rows = len(self.data)
        cols = len(self.data[0])

        result = []

        for i in range(rows):
            row = []
            for j in range(cols):
                value = self.data[i][j] + other.data[i][j]
                row.append(value)
            result.append(row)

        return Matrix(result)
    
    def __mul__(self, scalar):
        
        result = []

        for row in self.data:
            new_row = []
            for value in row:
                new_row.append(value * scalar)
            result.append(new_row)

        return Matrix(result)
    
    def __matmul__(self, other):
        rows_a = len(self.data)
        cols_a = len(self.data[0])

        rows_b = len(other.data)
        cols_b = len(other.data[0])

        if cols_a != rows_b:
            raise ValueError("Number of columns in first matrix must be equal to the number of rows in second matrix.")
        
        result = []

        for i in range(rows_a):
            row = []
            for j in range(cols_b):
                total = 0
                for k in range(cols_a):
                    total += self.data[i][k] * other.data[k][j]
                row.append(total)
            result.append(row)
            
        return Matrix(result)
