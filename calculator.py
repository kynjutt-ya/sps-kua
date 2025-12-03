import math

# Получить площадь прямоугольного треугольника
def get_area(a, b):
	return a * b

if __name__ == "__main__":
	print("Введите a:")
	a = int(input())
	print("Введите b:")
	b = int(input())
	print("c =", get_hypotenuse(a, b))
	print("S =", get_area(a, b))
