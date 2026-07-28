# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def transpose_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    return transposed

def add_matrices(mat1, mat2):
    rows, cols = len(mat1), len(mat1[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = mat1[i][j] + mat2[i][j]
    return  

def multiply_matrices(mat1, mat2):
    m, n, p = len(mat1), len(mat2), len(mat2[0])
    result = [[0 for _ in range(p)] for _ in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

print("Part A: Transpose")
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = []
for i in range(rows):
    row = list(map(int, input(f"Enter row {i+1}: ").split()))
    matrix.append(row)

print("\nOriginal Matrix:")
print_matrix(matrix)
transposed = transpose_matrix(matrix)
print("\nTransposed Matrix:")
print_matrix(transposed)

print("\nPart B: Add Matrices")
mat1 = matrix
mat2 = []
for i in range(rows):
    row = list(map(int, input(f"Enter row {i+1} of second matrix: ").split()))
    mat2.append(row)

print("\nMatrix 1:")
print_matrix(mat1)
print("\nMatrix 2:")
print_matrix(mat2)
added = add_matrices(mat1, mat2)
print("\nSum:")
print_matrix(added)

print("\nPart C: Multiply Matrices")
m = int(input("Enter rows for A: "))
n = int(input("Enter cols for A/rows for B: "))
p = int(input("Enter cols for B: "))
A = []
B = []
for i in range(m):
    row = list(map(int, input(f"Enter row {i+1} of A: ").split()))
    A.append(row)
for i in range(n):
    row = list(map(int, input(f"Enter row {i+1} of B: ").split()))
    B.append(row)

    print("\nMatrix A:")
print_matrix(A)
print("\nMatrix B:")
print_matrix(B)
product = multiply_matrices(A, B)
print("\nProduct:")
print_matrix(product)