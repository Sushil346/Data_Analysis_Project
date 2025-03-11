import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(list).reshape(-1,3)
    allmean = [ np.mean(matrix, axis=0), np.mean(matrix, axis=1), np.mean(matrix) ]
    allvar = [ np.var(matrix, axis=0), np.var(matrix, axis=1), np.var(matrix) ]
    allstd = [ np.std(matrix, axis=0), np.std(matrix, axis=1), np.std(matrix) ]
    allmax = [ np.max(matrix, axis=0), np.max(matrix, axis=1), np.max(matrix) ]
    allmin = [ np.min(matrix, axis=0), np.min(matrix, axis=1), np.min(matrix) ]
    allsum = [ np.sum(matrix, axis=0), np.sum(matrix, axis=1), np.sum(matrix) ]

    calculations = {        
        'mean' : allmean,
        'variance' : allvar,
        'Standard deviation' : allstd,
        'max' : allmax,
        'min' : allmin,
        'sum' : allsum,
     }

    return calculations