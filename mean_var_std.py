import numpy as np


def calculate(data):
    if len(data) != 9:
        raise ValueError("List must contain 9 numbers")

    arr = np.array(data).reshape(3, 3)

    result = {}

    mean_h = np.mean(arr, axis=0).tolist()
    mean_v = np.mean(arr, axis=1).tolist()
    mean_f = np.mean(arr)

    result["mean"] = [mean_h, mean_v, mean_f]

    variance_h = np.var(arr, axis=0).tolist()
    variance_v = np.var(arr, axis=1).tolist()
    variance_f = np.var(arr)

    result["variance"] = [variance_h, variance_v, variance_f]

    std_h = np.std(arr, axis=0).tolist()
    std_v = np.std(arr, axis=1).tolist()
    std_f = np.std(arr)

    result["standard deviation"] = [std_h, std_v, std_f]

    max_h = np.max(arr, axis=0).tolist()
    max_v = np.max(arr, axis=1).tolist()
    max_f = np.max(arr)

    result["max"] = [max_h, max_v, max_f]

    min_h = np.min(arr, axis=0).tolist()
    min_v = np.min(arr, axis=1).tolist()
    min_f = np.min(arr)

    result["min"] = [min_h, min_v, min_f]

    sum_h = np.sum(arr, axis=0).tolist()
    sum_v = np.sum(arr, axis=1).tolist()
    sum_f = np.sum(arr)

    result["sum"] = [sum_h, sum_v, sum_f]
    return result


data = [0, 1, 2, 3, 4, 5, 6, 7, 8]
summary = calculate(data)

for key, value in summary.items():
    print(key, value)
