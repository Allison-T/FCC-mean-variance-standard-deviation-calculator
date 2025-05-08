import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    num_array = np.array(list).reshape((3,3))

    calculations = {
        'mean': [num_array.mean(axis=0).tolist(),
                 num_array.mean(axis=1).tolist(),
                 num_array.mean()],
        'variance': [
                 num_array.var(axis=0).tolist(),
                 num_array.var(axis=1).tolist(),
                 num_array.var()
        ],
        'standard deviation': [
                 num_array.std(axis=0).tolist(),
                 num_array.std(axis=1).tolist(),
                 num_array.std()
        ],
        'max': [
                 num_array.max(axis=0).tolist(),
                 num_array.max(axis=1).tolist(),
                 num_array.max()],
        'min': [
                 num_array.min(axis=0).tolist(),
                 num_array.min(axis=1).tolist(),
                 num_array.min()],
        'sum': [
                 num_array.sum(axis=0).tolist(),
                 num_array.sum(axis=1).tolist(),
                 num_array.sum()],  

    }

    return calculations