def sum_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_numbers(n - 1)

def main():
    result = sum_numbers(10)
    print(f"The sum of numbers from 0 to 10 is: {result}")

if __name__ == "__main__":
    main()
