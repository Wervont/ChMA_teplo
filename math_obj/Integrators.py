import numpy as np

def euler_method_newton_teplo(f, T0, T_env, gamma, x0, x_end, h):
    # Число шагов
    n_steps = int((x_end - x0) / h)

    # Инициализация массивов для хранения результатов
    x_values = np.linspace(x0, x_end, n_steps + 1)
    T_values = np.zeros(n_steps + 1)

    # Начальные условия
    T_values[0] = T0

    # Итерации метода Эйлера
    for i in range(n_steps):
        T_values[i + 1] = T_values[i] + h * f(T_values[i], T_env, gamma)

    return x_values, T_values


# Модифицированный метод Эйлера (Эйлера-Коши)
def modified_euler_method_newton_teplo(f, T0, T_env, gamma, x0, x_end, h):
    # Число шагов
    n_steps = int((x_end - x0) / h)

    # Инициализация массивов для хранения результатов
    x_values = np.linspace(x0, x_end, n_steps + 1)
    T_values = np.zeros(n_steps + 1)

    # Начальные условия
    T_values[0] = T0

    # Итерации модифицированного метода Эйлера
    for i in range(n_steps):
        # Прогнозирующее значение
        T_predict = T_values[i] + h * f(T_values[i], T_env, gamma)

        # Корректирующее значение
        T_values[i + 1] = T_values[i] + h * f((T_values[i] + T_predict) / 2, T_env, gamma)

    return x_values, T_values

