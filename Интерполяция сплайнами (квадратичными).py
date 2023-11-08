import numpy as np

#print('Введите количество имеющихся точек')
#n= (int(input()))
#a=[]
#b=[]
#for i in range (n):
#    print('Введите значение координату х точки', i+1)
 #   a.append(float(input()))
  #  print('Введите значение координату y точки', i+1)
   # b.append(float(input()))
#xval = np.array(a, float)
#yval = np.array(b, float)

# Define the x and y values
xval = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], float)
yval = np.array([0, 2.8, 2.03, -1.33, -2.99, -0.84, 2.38, 2.56, -0.52, -2.94], float)
xi = float(input('Введите точку в которой хотите посчитать значение:'))
print()
# Function to calculate the coefficients for quadratic interpolation
def quadratic_interpolation(x, y):
    n = len(x)

    # Calculate the differences between x values and y values
    h = [x[i + 1] - x[i] for i in range(n - 1)]
    alpha = [(y[i + 1] - y[i]) / h[i] for i in range(n - 1)]

    # Initialize A and B as zero matrices
    A = np.zeros((n, n))
    B = np.zeros(n)

    # Set the first and last elements of A and B
    A[0, 0] = 1
    A[n - 1, n - 1] = 1
    B[0] = 0
    B[n - 1] = 0

    # Calculate the elements of A and B
    for i in range(1, n - 1):
        A[i, i - 1] = h[i - 1]
        A[i, i] = 2 * (h[i - 1] + h[i])
        A[i, i + 1] = h[i]
        B[i] = 3 * (alpha[i] - alpha[i - 1])

    # Solve the system of linear equations to get c
    c = np.linalg.solve(A, B)

    # Calculate a and b
    a = y[:-1]
    b = [alpha[i] - c[i] * h[i] for i in range(n - 1)]

    # Combine a, b and c into coefficients
    coefficients = list(zip(a, b, c[:-1]))
    print("\n".join(map(str, coefficients)))
    return coefficients


# Calculate the coefficients using the function
coefficients = quadratic_interpolation(xval, yval)


# Function to evaluate the quadratic spline at a given x value (xi)
def evaluate_quadratic_spline(coefficients, x, xi):
    for i in range(len(x) - 1):
        if x[i] <= xi <= x[i + 1]:
            a, b, c = coefficients[i]
            dx = xi - x[i]
            result = a + b * dx + c * dx ** 2
            return result
    return None


# Ask the user for an x value and calculate the corresponding y value

interpolated_value = evaluate_quadratic_spline(coefficients, xval, xi)
print()
# Print the result
print(f"Значение функции при x={xi}: {round(interpolated_value,3)}")
print('------------------------------------------------------------------------------------------')
print(f"Значение функции при x={0.5}: {round(evaluate_quadratic_spline(coefficients, xval, 0.5),3)}")
print(f"Значение функции при x={1.5}: {round(evaluate_quadratic_spline(coefficients, xval, 1.5),3)}")
print(f"Значение функции при x={2.5}: {round(evaluate_quadratic_spline(coefficients, xval, 2.5),3)}")
print(f"Значение функции при x={3.5}: {round(evaluate_quadratic_spline(coefficients, xval, 3.5),3)}")
print(f"Значение функции при x={4.5}: {round(evaluate_quadratic_spline(coefficients, xval, 4.5),3)}")
print(f"Значение функции при x={5.5}: {round(evaluate_quadratic_spline(coefficients, xval, 5.5),3)}")
print(f"Значение функции при x={6.5}: {round(evaluate_quadratic_spline(coefficients, xval, 6.5),3)}")
print(f"Значение функции при x={7.5}: {round(evaluate_quadratic_spline(coefficients, xval, 7.5),3)}")
print(f"Значение функции при x={8.5}: {round(evaluate_quadratic_spline(coefficients, xval, 8.5),3)}")
