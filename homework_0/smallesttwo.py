import sys

def main():
    #DOing a set so it doesn't have repeat
    numbers = set()

    # Read all ints from standard input
    for token in sys.stdin.read().split():
        numbers.add(int(token))

    # have a minimum variable and second minimum vairable
    min_val = float('inf')
    second_min = float('inf')

    for num in numbers:
        if num < min_val:
            second_min = min_val
            min_val = num
        elif num < second_min:
            second_min = num

    # proitning out the min and second min
    print(min_val)
    print(second_min)

if __name__ == "__main__":
    main()
