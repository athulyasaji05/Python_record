def find_numbers_and_sum():
    start = 101
    end = 199
    divisible_by = 7

    numbers = [i for i in range(start, end + 1) if i % divisible_by == 0]
    count = len(numbers)
    total_sum = sum(numbers)

    return count, total_sum

def main():
    count, total_sum = find_numbers_and_sum()
    print(f"Number of integers greater than 100 and less than 200 that are divisible by 7: {count}")
    print(f"Sum of these integers: {total_sum}")

if __name__ == "__main__":
    main()
