"""
Test Driven Doc import
Don't import using __import__
"""

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")

def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix
    Args:
    matrix: defines the matrix
    div: number to divide by
    matrix must be a list of lists of integers or floats
    Each row of the matrix must be of the same size
    div must be a number (integer or float)
    div can't be equla to 0.
    All elements of the matrix are divided by div, rounded to 2 decimal places
    Returns: a new matrix
    """
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    length = None
    for i in matrix:
        if type(i) != list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if length is None:
            length = len(i)
        if length != len(i):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if type(j) != int and type(j) != float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for j in i:
        new_matrix.append()
    return
