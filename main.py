import numpy as np

# Крок 1. Введення даних
N = 3  # кількість функціоналів оцінювання
l = 2  # кількість інформаційних ситуацій
m = 4  # кількість рішень
n = 3  # кількість економічних станів

# Множина рішень X
X = np.array([10, 20, 30, 40])  # значення для кожного рішення

# Множина економічних станів Theta
Theta = np.array([0.3, 0.5, 0.2])  # ймовірності для кожного стану

# Коефіцієнти пріоритетів для згортки функціоналів
priority_coefficients = np.array([0.4, 0.35, 0.25])  # для кожного функціоналу

# Крок 2. Функціонали оцінювання
def F1(x):
    return x * 0.8  # перший функціонал (може представляти, наприклад, дохід)

def F2(x):
    return x * 0.6  # другий функціонал (наприклад, інвестиції)

def F3(x):
    return x * 0.9  # третій функціонал (наприклад, ризики)

# Крок 3. Обчислення функціоналів для кожного рішення
def calculate_functionals(X):
    F1_values = np.array([F1(x) for x in X])
    F2_values = np.array([F2(x) for x in X])
    F3_values = np.array([F3(x) for x in X])
    return F1_values, F2_values, F3_values

F1_values, F2_values, F3_values = calculate_functionals(X)

# Крок 4. Згортка функціоналів оцінювання
def integrate_functionals(F1_values, F2_values, F3_values, priority_coefficients):
    # Згортка для кожного рішення
    integrated_values = (priority_coefficients[0] * F1_values +
                         priority_coefficients[1] * F2_values +
                         priority_coefficients[2] * F3_values)
    return integrated_values

integrated_values = integrate_functionals(F1_values, F2_values, F3_values, priority_coefficients)

# Крок 5. Компромісне рішення з урахуванням ймовірностей економічних станів
def calculate_expected_values(integrated_values, Theta):
    # Очікуване значення для кожного рішення, з урахуванням станів економічного середовища
    expected_values = np.sum(integrated_values[:, np.newaxis] * Theta, axis=1)
    return expected_values

# Розрахунок компромісного рішення
expected_values = calculate_expected_values(integrated_values, Theta)

# Пошук оптимального рішення
optimal_index = np.argmax(expected_values)
optimal_decision = X[optimal_index]

print("Очікувані значення для кожного рішення:", expected_values)
print("Компромісне рішення:", optimal_decision)
