import sys

def main():
    if len(sys.argv) != 3:
        print("Использование: python task4.py <path_to_circle_data.txt> <path_to_dots_data.txt>")
        return

    path_to_circle_data = sys.argv[1]
    path_to_dots_data = sys.argv[2]

    circle_data = []

    # Читаем данные окружности
    try:
        with open(path_to_circle_data, 'r') as file:
            x_center, y_center = map(float, file.readline().strip().split())  # Читаем координаты центра
            radius = float(file.readline().strip())  # Читаем радиус
            circle_data = [x_center, y_center, radius]
    except FileNotFoundError:
        print("Файл не найден")
        return
    except ValueError:
        print("Некорректный формат данных в файле окружности")
        return

    # Читаем точки
    try:
        with open(path_to_dots_data, 'r') as file:
            for line in file:
                x, y = map(float, line.strip().split())
                solver(x, y, circle_data)
    except FileNotFoundError:
        print("Файл не найден")
        return
    except ValueError:
        print("Некорректный формат данных в файле точек")
        return


def solver(x, y, circle_data):
    x_center, y_center, radius = circle_data
    value = (x - x_center) ** 2 + (y - y_center) ** 2 - radius ** 2
    if value == 0:
        print(0)
    elif value < 0:
        print(1)
    else:
        print(2)

if __name__ == "__main__":
    main()