import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Чтение данных из CSV файла
data = pd.read_csv('../data/data.csv')

# Данные из файла
x_csv = data['x']
y_csv = data['y']

# Функция для вычисления температуры при данном значении gamma
def temperature_model(gamma, T0, T_env, x):
    return T_env + (T0 - T_env) * np.exp(-gamma * x)

# Функция для вычисления суммы квадратов отклонений (ошибки)
def objective_function(gamma, T0, T_env, x_csv, y_csv):
    y_model = temperature_model(gamma, T0, T_env, x_csv)
    return np.sum((y_model - y_csv) ** 2)

# Начальные параметры
T0 = 83
T_env = 22
initial_gamma = 0.045

# Минимизация ошибки для нахождения оптимального gamma
result = minimize(objective_function, initial_gamma, args=(T0, T_env, x_csv, y_csv))

# Оптимальное значение gamma
optimal_gamma = result.x[0]
print(f"Оптимальное значение gamma: {optimal_gamma}")

# Вычисление температур с оптимальным gamma
y_optimized = temperature_model(optimal_gamma, T0, T_env, x_csv)

# Построение графиков
plt.plot(x_csv, y_csv, 'o', label='Табличные данные')
plt.plot(x_csv, y_optimized, '-', label=f'Модель с оптимальным gamma = {optimal_gamma:.5f}')
plt.xlabel('Время')
plt.ylabel('Температура')
plt.title('Подбор оптимального значения gamma')
plt.legend()
plt.grid(True)
plt.show()
