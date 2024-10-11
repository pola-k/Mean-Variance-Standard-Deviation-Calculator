# Mean, Variance, Standard Deviation Calculator

This project is part of **freeCodeCamp's Data Analysis with Python** course. It involves using Numpy to compute various statistical measures (mean, variance, standard deviation, maximum, minimum, and sum) along the rows, columns, and for the entire matrix of a 3x3 array.

## Project Overview

The main objective of this project is to create a function `calculate()` that takes a list of 9 numbers as input, converts it into a 3x3 Numpy array, and returns a dictionary containing statistical metrics computed along both axes and for the flattened matrix.

### Function Requirements:
1. **Input**: A list containing 9 digits.
- If the list contains less than 9 elements, raise a `ValueError`.

2. **Output**: A dictionary with the following keys:
- `'mean'`: Mean of the values along both axes and the flattened array.
- `'variance'`: Variance of the values along both axes and the flattened array.
- `'standard deviation'`: Standard deviation of the values along both axes and the flattened array.
- `'max'`: Maximum value along both axes and the flattened array.
- `'min'`: Minimum value along both axes and the flattened array.
- `'sum'`: Sum of the values along both axes and the flattened array.

Each value in the dictionary should be a list of three elements:
- The first element is the result for axis 0 (columns),
- The second element is the result for axis 1 (rows),
- The third element is the result for the flattened matrix.

### Example

If the input list is:
```python
calculate([0,1,2,3,4,5,6,7,8])
```

The output should be:
```python
{
'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
'max': [[6, 7, 8], [2, 5, 8], 8],
'min': [[0, 1, 2], [0, 3, 6], 0],
'sum': [[9, 12, 15], [3, 12, 21], 36]
}
```

### How to Run the Script
1. Clone this repository or download the code.
2. Install Numpy using `pip install numpy`.
3. Run the Python script using the following command:
```bash
python mean_var_std.py
```

### Key Functions Used
- **`np.mean()`**: To calculate the mean.
- **`np.var()`**: To calculate the variance.
- **`np.std()`**: To calculate the standard deviation.
- **`np.max()`**: To calculate the maximum value.
- **`np.min()`**: To calculate the minimum value.
- **`np.sum()`**: To calculate the sum of elements.

This function is designed to handle only 9-element lists. It throws a `ValueError` if the list length is incorrect, ensuring the correct input format is used.

## Conclusion

This project demonstrates basic matrix manipulation and statistical calculations using Numpy. By converting a list of numbers into a 3x3 matrix, we can analyze and compute meaningful statistics across the matrix's rows, columns, and entire structure.
