def is_substring(main_string, sub_string):
    return sub_string in main_string

def count_occurrences(main_string, char):
    return main_string.count(char)

def replace_substring(main_string, old_substring, new_substring):
    return main_string.replace(old_substring, new_substring)

def convert_to_capital(main_string):
    return main_string.upper()

def menu():
    print("Menu:")
    print("1. Check if the String is a Substring of Another String")
    print("2. Count Occurrences of Character")
    print("3. Replace a Substring with Another Substring")
    print("4. Convert to Capital Letters")
    print("5. Exit")

def main():
    while True:
        menu()
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            main_string = input("Enter the main string: ")
            sub_string = input("Enter the substring to check: ")
            if is_substring(main_string, sub_string):
                print(f"'{sub_string}' is a substring of '{main_string}'")
            else:
                print(f"'{sub_string}' is not a substring of '{main_string}'")

        elif choice == '2':
            main_string = input("Enter the main string: ")
            char = input("Enter the character to count: ")
            count = count_occurrences(main_string, char)
            print(f"The character '{char}' occurs {count} times in '{main_string}'")

        elif choice == '3':
            main_string = input("Enter the main string: ")
            old_substring = input("Enter the substring to replace: ")
            new_substring = input("Enter the new substring: ")
            result = replace_substring(main_string, old_substring, new_substring)
            print(f"The new string is: '{result}'")

        elif choice == '4':
            main_string = input("Enter the main string: ")
            result = convert_to_capital(main_string)
            print(f"The string in capital letters is: '{result}'")

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
