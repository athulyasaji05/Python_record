import os

def remove_file(file_path):
    try:
        # Check file attributes
        print(f"File attributes for '{file_path}':")
        os.system(f'attrib "{file_path}"')

        # Try to remove the file
        os.remove(file_path)
        print(f"File '{file_path}' removed successfully.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"Error occurred while removing file '{file_path}': {e}")

def main():
    file_path = input("Enter the file path to remove: ")
    remove_file(file_path)

if __name__ == "__main__":
    main()
