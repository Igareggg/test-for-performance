import sys

def main():
    if len(sys.argv) != 2:  
        print("Использование: python task4.py <test.txt>")
        return

    arr = []
    try:
        with open(sys.argv[1], 'r') as file:
            arr = list(map(int, file.readlines()))
    except IOError as e:
        print(e, file=sys.stderr)

    length = len(arr)
    counter = 0
    total_sum = sum(arr)

    mean = total_sum // length 

    for index in range(length):
        while arr[index] < mean:
            arr[index] += 1
            counter += 1
        while arr[index] > mean:
            arr[index] -= 1
            counter += 1

    print(counter)

if __name__ == "__main__":
    main()