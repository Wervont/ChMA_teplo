
def f_prch_newton_teplo(T, T_env, gamma):

    dy_dx = -gamma*(T - T_env)

    return dy_dx