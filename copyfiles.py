def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as f_source:
            with open(destination_file, 'w') as f_dest:
                for line in f_source:
                    f_dest.write(line)
        print(f"Contents of {source_file} copied to {destination_file} successfully.")
    except FileNotFoundError:
        print("Error: One or both files not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    source_file = input("Enter the source file name: ")
    destination_file = input("Enter the destination file name: ")

    copy_file(source_file, destination_file)

if __name__ == "__main__":
    main()
