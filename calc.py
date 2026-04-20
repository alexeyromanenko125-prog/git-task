# Автор: Алексей Романенко
import math

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a*b #Исправлено

def sqrt(x):
    if x < 0:
        raise ValueError("Вещественный квадратный корень из отрицательного числа не существует")
    return math.sqrt(x)

if __name__ == "__main__":
    print("Простой калькулятор запущен.")
    print(f"2 + 2 = {add(2, 2)}")
"# trigger" 
