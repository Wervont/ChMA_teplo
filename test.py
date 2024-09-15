import matplotlib.pyplot as plt
import numpy as np

def euler_method(T0, T_env, gamma, dt, time_end):
    """
    Решение уравнения теплопроводности Ньютона методом Эйлера.

    :param T0: начальная температура (в градусах Цельсия)
    :param T_env: температура окружающей среды (в градусах Цельсия)
    :param gamma: коэффициент теплопроводности
    :param dt: шаг по времени
    :param time_end: конечное время (в минутах)
    :return: список времени и соответствующих температур
    """
    times = [0]  # начальное время
    temperatures = [T0]  # начальная температура

    t = 0
    T = T0

    while t < time_end:
        dT = -gamma * (T - T_env) * dt  # изменение температуры по уравнению Ньютона
        T += dT  # новая температура
        t += dt  # новый момент времени

        times.append(t)
        temperatures.append(T)

    return times, temperatures

# Параметры задачи
T0 = 83  # начальная температура кофе (°C)
T_env = 22  # температура окружающей среды (°C)
gamma = 0.044 # коэффициент теплопроводности
dt = 0.1  # шаг по времени (минуты)
time_end = 15  # время моделирования (минуты)

# Решение задачи
times, temperatures = euler_method(T0, T_env, gamma, dt, time_end)


x = np.linspace(0, 15, 16)
y = [83, 77.7, 75.1, 73, 71.1, 69.4, 67.8, 66.4, 64.7, 63.4, 62.1, 61, 59.9, 58.7, 57.8, 56.6]

# Построение графика
plt.plot(times, temperatures, label='Температура кофе')
plt.plot(x, y)
plt.xlabel('Время (мин)')
plt.ylabel('Температура (°C)')
plt.title('Остывание кофе по закону Ньютона')
plt.axhline(y=T_env, color='r', linestyle='--', label='Температура окружения')
plt.legend()
plt.grid(True)
plt.show()
