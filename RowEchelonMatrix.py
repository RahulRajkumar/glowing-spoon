import numpy as np
from random import randint

# Random (row, 1byN) vector with specified leading entry in specified
# index (mathematician 1-indexing) by left-padding with zeros and
# right-padding with random [0,9]-integers
def random_vector_specified_leading_entry(x,j,N):
    left_padding = [0 for i in range(j-1)]
    right_padding = [randint(0,9) for i in range(N - j)]
    vector = []
    vector.extend(left_padding)
    vector.extend([x])
    vector.extend(right_padding)
    return(np.array(vector))

# Random MbyN matrix in row echelon form with pivots in the specified
# pivot_columns taking the specified pivot_values
def random_row_echelon_specified_pivots(pivot_columns,pivot_values,M,N):
    rows = []

    for i in range(len(pivot_columns)):
        x = pivot_values[i]
        j = pivot_columns[i]
        row_i = random_vector_specified_leading_entry(x,j,N)
        rows.append(row_i)

    m = len(rows)
    if m < M:
        for i in range(M - m):
            rows.append([0 for j in range(N)])
        
    return(np.array(rows))
    
