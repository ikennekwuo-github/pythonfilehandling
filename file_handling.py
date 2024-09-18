# file_handling_assignment

def create_file():
    try:
        with open("my_file.text", 'w') as file:
            file.write("Hello, World!\n")
            file.write("This is a line of text.\n")
            file.write("Here is a number: 42\n")
        print("File created and initial content written successfully.")
    except Exception as e:
        print(f"An error occured while createing the file: {e}")

def read_file():
    try:
        with open("my_file.txt", 'r') as file:
            content = file.read()
            print("\nContents of 'my_file.txt':")
            print(content)
    except FileNotFoundError:
        print("The file does not exist.")
    except PermissionError:
        print("Permission denied while trying to read the file.")
    except Exception as e:
        print(f"An error occured while reading the file: {e}")

def append_to_file():
    try:
        with open("my_file.txt", 'a') as file:
            file.write("Appending another line.\n")
            file.write("Here is another number: 99\n")
            file.write("This is the final line.\n")
        print("Additional content appended successfully.")
    except FileNotFoundError:
        print("The file does not exist.")
    except PermissionError:
        print("Permission denied while trying to append to the file.")
    except Exception as e:
        print(f"An error occured while appending to the file: {e}")

def main():
    create_file()
    read_file()
    append_to_file()
    read_file()

if __name__ == "__main__":
    main()                   