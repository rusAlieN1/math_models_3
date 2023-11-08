import numpy as np
import math

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
z = float(input('Введите точку в которой хотите посчитать значение:'))

def calculate(x, y):
    print()
    n = len(x)
    p = np.zeros([n, n+1])

    for i in range(n):
        p[i, 0] = y[i]

    for i in range(1, n):
        for j in range(n - i):
            p[j][i] = (p[j + 1][i - 1] - p[j][i - 1])
    return p

p=calculate(xval, yval)
n1 = len(xval)
for i in range(n1):
    for j in range(n1 - i):
        print(p[i][j], end="\t")
    print("")

def interpol(x, y, z):
    n = len(x)
    p = calculate(x, y)

    sum = p[0][0]
    s = (z - x[0]) / (x[1] - x[0])

    for i in range(1, n):
        sum += (s * p[0][i]) / math.factorial(i)
        s *= (z - x[i])
    return sum
result = interpol(xval, yval, z)
print()
print(f"Значение функции при x={z}: {round(result, 3)}")
print('------------------------------------------------------------------------------------------')
print(f"Значение функции при x={0.5}: {round(interpol(xval, yval, 0.5), 3)}")
print(f"Значение функции при x={1.5}: {round(interpol(xval, yval, 1.5), 3)}")
print(f"Значение функции при x={2.5}: {round(interpol(xval, yval, 2.5), 3)}")
print(f"Значение функции при x={3.5}: {round(interpol(xval, yval, 3.5), 3)}")
print(f"Значение функции при x={4.5}: {round(interpol(xval, yval, 4.5), 3)}")
print(f"Значение функции при x={5.5}: {round(interpol(xval, yval, 5.5), 3)}")
print(f"Значение функции при x={6.5}: {round(interpol(xval, yval, 6.5), 3)}")
print(f"Значение функции при x={7.5}: {round(interpol(xval, yval, 7.5), 3)}")
print(f"Значение функции при x={8.5}: {round(interpol(xval, yval, 8.5), 3)}")
