import numpy as np
def get_determinant(matrix):
    array = np.array(matrix)
    if(array.shape[0] != array.shape[1]):
        return("The matrix must be square to compute the determinant")
    
    