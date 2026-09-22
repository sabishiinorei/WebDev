# Задача №1
# TAX_RATE = 0.13

# income = float(input("Введите ваш годовой доход (в рублях): "))

# tax_amount = income * TAX_RATE
# net_income = income - tax_amount

# print(
#     f"Общая сумма дохода:                  "
#     f"{income:,.2f} руб.".replace(",", " ")
# )
# print(
#     f"Сумма рассчитанного налога (13%):    "
#     f"{tax_amount:,.2f} руб.".replace(",", " ")
# )
# print(
#     f"Сумма «на руки» после вычета налога: "
#     f"{net_income:,.2f} руб.".replace(",", " ")
# )



# Задача №2
# weight, height = map(
#     float,
#     input("Введите ваш вес (кг) и рост в метрах (м) через пробел: ").split(),
# )

# bmi = weight / (height**2)

# print(f"Ваш индекс массы тела (ИМТ): {bmi:.1f}")



# Задача №3
# USD_TO_RUB = 95.50

# def convert_usd_to_rub(amount_usd: float) -> float:
#     """Конвертирует сумму из долларов США (USD) в рубли (RUB).

#     Args:
#         amount_usd (float): Сумма в долларах.

#     Returns:
#         float: Эквивалентная сумма в рублях.
#     """
#     return amount_usd * USD_TO_RUB


# usd_amount = float(input("Введите сумму в долларах ($): "))
# rub_amount = convert_usd_to_rub(usd_amount)

# print(
#     f"Сумма в рублях по курсу {USD_TO_RUB}: "
#     f"{rub_amount:,.2f} руб.".replace(",", " ")
# )



# Задача №4
# import math

# def calculate_rectangle_area(width: float, height: float) -> float:
#     """Вычисляет площадь прямоугольника.

#     Args:
#         width (float): Ширина.
#         height (float): Высота.

#     Returns:
#         float: Площадь прямоугольника.
#     """
#     return width * height


# def calculate_circle_area(radius: float) -> float:
#     """Вычисляет площадь круга.

#     Args:
#         radius (float): Радиус круга.

#     Returns:
#         float: Площадь круга.
#     """
#     return math.pi * (radius**2)


# rect_w, rect_h = map(
#     float,
#     input("Введите ширину и высоту прямоугольника через пробел: ").split(),
# )
# rect_area = calculate_rectangle_area(rect_w, rect_h)
# print(f"Площадь прямоугольника: {rect_area:.2f}")

# circle_r = float(input("Введите радиус круга: "))
# circle_area = calculate_circle_area(circle_r)
# print(f"Площадь круга: {circle_area:.2f}")



# Задача №5
# amount = int(input("Введите сумму для снятия (кратно 100): "))

# n5000 = amount // 5000
# rem = amount % 5000

# n2000 = rem // 2000
# rem = rem % 2000

# n1000 = rem // 1000
# rem = rem % 1000

# n500 = rem // 500
# rem = rem % 500

# n200 = rem // 200
# rem = rem % 200

# n100 = rem // 100

# print(f"\nВыдача купюр для суммы {amount} руб.:")
# print(f"5000 руб.: {n5000} шт.")
# print(f"2000 руб.: {n2000} шт.")
# print(f"1000 руб.: {n1000} шт.")
# print(f" 500 руб.: {n500} шт.")
# print(f" 200 руб.: {n200} шт.")
# print(f" 100 руб.: {n100} шт.")



# Задача №6
# import math


# def calculate_distance(x1: float, y1: float, x2: float, y2: float) -> float:
#     """Вычисляет евклидово расстояние между двумя точками.

#     Args:
#         x1, y1 (float): Координаты первой точки.
#         x2, y2 (float): Координаты второй точки.

#     Returns:
#         float: Расстояние между точками.
#     """
#     return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# def calculate_triangle_area(a: float, b: float, c: float) -> float:
#     """Вычисляет площадь треугольника по формуле Герона.

#     Args:
#         a, b, c (float): Длины сторон треугольника.

#     Returns:
#         float: Площадь треугольника.
#     """
#     s = (a + b + c) / 2 
#     return math.sqrt(s * (s - a) * (s - b) * (s - c))


# x1, y1 = map(float, input("Введите координаты точки A (x y): ").split())
# x2, y2 = map(float, input("Введите координаты точки B (x y): ").split())
# x3, y3 = map(float, input("Введите координаты точки C (x y): ").split())

# side_a = calculate_distance(x1, y1, x2, y2)
# side_b = calculate_distance(x2, y2, x3, y3)
# side_c = calculate_distance(x3, y3, x1, y1)

# area = calculate_triangle_area(side_a, side_b, side_c)

# print(f"Площадь треугольника: {area:.2f}")



# Задача №7
# FUEL_PRICE_PER_LITER = 49.50


# def calculate_trip_cost(
#     distance_km: float, consumption_per_100km: float
# ) -> tuple[float, float]:
#     """Рассчитывает необходимый объем бензина и полную стоимость поездки.

#     Args:
#         distance_km (float): Расстояние поездки в километрах.
#         consumption_per_100km (float): Расход топлива (литров на 100 км).

#     Returns:
#         tuple[float, float]: Кортеж из двух значений:
#                              1) Объем бензина в литрах.
#                              2) Стоимость поездки в рублях.
#     """
#     fuel_required = distance_km * (consumption_per_100km / 100)
#     total_cost = fuel_required * FUEL_PRICE_PER_LITER
#     return fuel_required, total_cost


# distance = float(input("Какое расстояние поездки (км)? "))
# consumption = float(input("Сколько литров на 100 км ест машина? "))

# fuel_needed, trip_price = calculate_trip_cost(distance, consumption)

# print(f"Необходимо бензина: {fuel_needed:.2f} л")
# print(f"Стоимость поездки: {trip_price:.2f} руб.")
