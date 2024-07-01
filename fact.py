factorial_cache = {}

def factorial(n):
    if n in factorial_cache:
        return factorial_cache[n]
    
    if n == 0 or n == 1:
        factorial_cache[n] = 1
    else:
        factorial_cache[n] = n * factorial(n - 1)
    
    return factorial_cache[n]

def main():
    while True:
        try:
            number = int(input("Enter a number to find its factorial (or a negative number to exit): "))
            if number < 0:
                print("Exiting the program.")
                break
            result = factorial(number)
            print(f"The factorial of {number} is: {result}")
            print(f"Factorial cache: {factorial_cache}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
