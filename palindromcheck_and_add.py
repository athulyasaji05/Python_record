def is_palindrome(number):
    return str(number) == str(number)[::-1]

def reverse_number(number):
    return int(str(number)[::-1])

def find_palindrome(number):
    while not is_palindrome(number):
        reversed_number = reverse_number(number)
        number += reversed_number
        print(f"Intermediate sum: {number}")
    return number

def main():
    number = int(input("Enter a number: "))
    palindrome = find_palindrome(number)
    print(f"The resulting palindrome is: {palindrome}")

if __name__ == "__main__":
    main()
