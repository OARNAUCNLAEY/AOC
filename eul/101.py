polynomial_hard = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]
polynomial_easy = [0, 0, 0, 1]
def generate_values(polynomial):
    values = []
    for x in range(1,len(polynomial) + 10):
        val = 0
        for i in range(len(polynomial)):
            val += polynomial[i] * (x ** i)
        values.append(val)
    return values
def get_coefficients(degree_allowed, values):
    value_matrix = []
    for i in range(1, len(values) + 1):
        row = []
        for d in range(degree_allowed):
            row.append(i ** d)
        value_matrix.append(row)
    import numpy as np
    coeffs = np.linalg.solve(np.array(value_matrix, dtype=np.int64), np.array(values, dtype = np.int64))
    # coeffs = np.linalg.lstsq(np.array(value_matrix, dtype=int), np.array(values, dtype = int), rcond=None)[0]
    return coeffs
def get_next_value(coeffs, x):
    val = 0
    for i in range(len(coeffs)):
        val += coeffs[i] * (x ** i)
    return val
values = generate_values(polynomial_hard)
print(values)
total_sum = 0
for i in range(len(polynomial_hard)):
    coeff = get_coefficients(i + 1, values[:i + 1])
    # for j in range(len(coeff)):
    #     coeff[j] = round(coeff[j])
    for j in range(len(coeff) + 1):
        print(f"Value for x={j + 1}: {round(get_next_value(coeff, j + 1))}")
    print(values)
    print(f"Degree {i}:, Next Value: {get_next_value(coeff, i + 2)}, value: {values[i + 1]}")
    total_sum += round(get_next_value(coeff, i + 2))
print(total_sum)
print(len(polynomial_hard))