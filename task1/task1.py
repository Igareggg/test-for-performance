def main():
    n = 0
    m = 0

    while n < 1 or m < 1:
        print("Введите 2 целых положительных числа через пробел: ", end="")
        input_values = input().split(" ")
        try:
            n = int(input_values[0])
            m = int(input_values[1])
        except (IndexError, ValueError):
            print("Некорректный ввод")

    result = "1"

    for i in range(1, n):
        index = (m - 1) * i
        element = (index + 1) % n
        element = n if element == 0 else element

        if element == 1:
            break

        result += str(element)

    print(result)

if __name__ == "__main__":
    main()