
class Figure:
    def __init__(self, coords: tuple, width: int | float, color: str):
        self.coords = coords  # кортеж координат
        self.width = width    # ширина
        self.color = color    # цвет

# 1 Класс Линия
class Line(Figure):
    def __init__(self, coords: tuple, width: int | float, color: str, length: float):
        super().__init__(coords, width, color)  
        self.length = length                    


# 2 Класс Прямоугольник
class Rect(Figure):
    def __init__(self, coords: tuple, width: int | float, color: str, height: float):
        super().__init__(coords, width, color)  
        self.height = height                    


# 3 Класс Эллипс
class Ellipse(Figure):
    def __init__(self, coords: tuple, width: int | float, color: str, radius: float):
        super().__init__(coords, width, color)  
        self.radius = radius                    


# === Создание объектов и вывод их свойств ===

line_obj = Line(coords=(0, 0, 10, 0), width=2, color="black", length=10.0)
rect_obj = Rect(coords=(5, 5), width=1, color="red", height=20.5)
ellipse_obj = Ellipse(coords=(10, 10), width=3, color="blue", radius=7.0)

print("--- Свойства Line ---")
print(f"Координаты: {line_obj.coords}")
print(f"Ширина: {line_obj.width}")
print(f"Цвет: {line_obj.color}")
print(f"Длина (уникальное): {line_obj.length}\n")

print("--- Свойства Rect ---")
print(f"Координаты: {rect_obj.coords}")
print(f"Ширина: {rect_obj.width}")
print(f"Цвет: {rect_obj.color}")
print(f"Высота (уникальное): {rect_obj.height}\n")

print("--- Свойства Ellipse ---")
print(f"Координаты: {ellipse_obj.coords}")
print(f"Ширина: {ellipse_obj.width}")
print(f"Цвет: {ellipse_obj.color}")
print(f"Радиус (уникальное): {ellipse_obj.radius}")
