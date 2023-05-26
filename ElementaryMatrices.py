###########################################################################
# Using the formulas in https://en.wikipedia.org/wiki/Elementary_matrix,  #
# provide functions that return 3x3 elementary row operation matrices     #
#                                                                         #
# Note that mathematicians' formulas assume 1-indexing and python         #
# assumes 0-indexing, hence index shifting occurs                         #
###########################################################################

import numpy as np

def exchange_rows(i,j):
    # Returns the elementary matrix that interchanges rows i and j
    
    xs = [[row_exchange_entries(i,j,k,l) for l in range(1,4)]
          for k in range(1,4)]
    return(np.array(xs))

def row_exchange_entries(i,j,k,l):
    if (k == j) and (l == i):
        return 1
    elif (k == j) and (l != i):
        return 0
    elif (k == i) and (l == j):
        return 1
    elif (k == i) and (l != j):
        return 0
    elif (k != i) and (k != j) and (k == l):
        return 1
    else:
        return 0

def multiply_row(i,m):
    # Returns the elementary matrix that multiplies elements in row i
    # by a nonzero scalar m

    if m == 0:
        raise ValueError("m must be nonzero")

    xs = [[row_multiply_entries(i,m,k,l) for l in range(1,4)]
          for k in range(1,4)]
    return(np.array(xs))
    
def row_multiply_entries(i,m,k,l):
    if (k == l) and (k == i):
        return m
    elif (k == l):
        return 1
    else:
        return 0

def add_rows(m,j,i):
    # Returns the elementary matrix that adds m times row j to row i
    
    xs = [[row_addition_entries(m,j,i,k,l) for l in range(1,4)]
          for k in range(1,4)]
    return(np.array(xs))

def row_addition_entries(m,j,i,k,l):
    if k == l:
        return 1
    elif (k == i) and (l == j):
        return m
    else:
        return 0
