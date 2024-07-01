def set_operations(set1, set2):
    while True:
        print("Set Operations Menu:")
        print("1. Set Union")
        print("2. Set Intersection")
        print("3. Set Difference")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            result = set1.union(set2)
            print(f"Union of sets: {result}")
        elif choice == '2':
            result = set1.intersection(set2)
            print(f"Intersection of sets: {result}")
        elif choice == '3':
            result = set1.difference(set2)
            print(f"Difference of sets (set1 - set2): {result}")
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def main():
    set1 = set(map(int, input("Enter the elements of the first set (separated by space): ").split()))
    set2 = set(map(int, input("Enter the elements of the second set (separated by space): ").split()))

    set_operations(set1, set2)

if __name__ == "__main__":
    main()
