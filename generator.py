import random
import math

# Крайние точки
west = (55.753125, 37.584025)   # Новый Арбат
east = (55.755266, 37.656652)   # Курская
north = (55.773320, 37.621042)  # Цветной бульвар
south = (55.730131, 37.623304)  # Добрынинская

# Центр эллипса
center_lat = (north[0] + south[0]) / 2
center_lon = (west[1] + east[1]) / 2

# Радиусы
radius_lat = (north[0] - south[0]) / 2
radius_lon = (east[1] - west[1]) / 2

def random_point_in_ellipse():
    # Случайный угол
    angle = random.uniform(0, 2 * math.pi)
    # Случайный радиус (sqrt для равномерного распределения)
    r = math.sqrt(random.uniform(0, 1))
    # Координаты внутри эллипса
    lat = center_lat + r * radius_lat * math.sin(angle)
    lon = center_lon + r * radius_lon * math.cos(angle)
    return lat, lon

if __name__ == "__main__":
    user_input = input("Стартуем?': ").strip().lower()
    if user_input == "поехали!":
        point = random_point_in_ellipse()
        print(f"Случайная точка внутри Садового кольца: {point[0]:.6f}, {point[1]:.6f}")
        print(f"Google Maps: https://www.google.com/maps?q={point[0]:.6f},{point[1]:.6f}")
    else:
        print("Не то слово, попробуй снова 🙂")
