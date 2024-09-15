import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Чтение данных из CSV файла
data = pd.read_csv('../data/data.csv')

# Данные из файла
x_csv = data['x']
y_csv = data['y']

# Имеющиеся данные для расчетов
T0 = 83
T_env = 22
# gamma = 0.038
gamma = 0.04196609200722465
x0 = 0
x_end = 15
h = 0.001

t = np.linspace(x0, x_end, 100)
T = T_env + (T0 - T_env) * np.exp(-gamma * t)

# Примерные данные для численных методов (замени на свои функции)
t_values = np.linspace(x0, x_end, int((x_end - x0) / h) + 1)
T_values = T_env + (T0 - T_env) * np.exp(-gamma * t_values)  # Эйлер Метод

t_values1 = t_values
T_values1 = T_env + (T0 - T_env) * np.exp(-gamma * t_values1 * 1.05)  # Модифицированный Эйлер Метод

# Построение графиков
plt.plot(t_values, T_values, color='b', label='Эйлер Метод')
# plt.plot(t_values1, T_values1, color='r', label='Модифицированный Эйлер Метод')
# plt.plot(t, T, color='black', label='Аналитическое решение')
plt.plot(x_csv, y_csv, color='green', marker='o', linestyle='--', label='Данные из CSV')

plt.xlabel('Время')
plt.ylabel('Температура')
plt.title('Сравнение численных методов и данных из файла')
plt.legend()
plt.grid(True)
plt.show()
