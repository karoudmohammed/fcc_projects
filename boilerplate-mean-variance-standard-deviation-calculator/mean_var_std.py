import numpy as np

def calculate(list):

    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    list = np.array(list, dtype=float)
    list = list.reshape(3, 3)

    mean = [
        np.mean(list, axis=0).tolist(),
        np.mean(list, axis=1).tolist(),
        np.mean(list.flatten())
    ]
    var = [np.var(list, axis=0).tolist(), np.var(list, axis=1).tolist(), np.var(list.flatten())]
    std = [np.std(list, axis=0).tolist(), np.std(list, axis=1).tolist(), np.std(list.flatten())]
    max = [np.max(list, axis=0).tolist(), np.max(list, axis=1).tolist(), np.max(list.flatten())]
    min = [np.min(list, axis=0).tolist(), np.min(list, axis=1).tolist(), np.min(list.flatten())]
    sum = [np.sum(list, axis=0).tolist(), np.sum(list, axis=1).tolist(), np.sum(list.flatten())]

    calculations = {
        'mean': mean,
        'variance': var,
        'standard deviation': std,
        'max': max,
        'min': min,
        'sum': sum
    }

    return calculations


print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))
