# File Creation
try:
    # Create a new text file named "my_file.txt" in write mode ('w')
    with open("my_file.txt", "w") as file:
        file.write("This is line 1\n")
        file.write("12345\n")
        file.write("Another line with some text and numbers: 789\n")
    print("File 'my_file.txt' created successfully and initial content written.")
except PermissionError:
    print("Permission denied to create file.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
finally:
    print("File creation process completed.\n")

# File Reading and Display
try:
    # Read the contents of "my_file.txt" and display them on the console
    with open("my_file.txt", "r") as file:
        print("Contents of 'my_file.txt':")
        for line in file:
            print(line.strip())  # Strip newlines for clean output
    print("\nFile content read and displayed successfully.")
except FileNotFoundError:
    print("File 'my_file.txt' not found.")
except PermissionError:
    print("Permission denied to read file.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
finally:
    print("File reading process completed.\n")

# File Appending
try:
    # Open "my_file.txt" in append mode ('a')
    with open("my_file.txt", "a") as file:
        file.write("Additional line 1\n")
        file.write("67890\n")
        file.write("Yet another line with some additional text: 543\n")
    print("Additional content appended to 'my_file.txt'.")
except FileNotFoundError:
    print("File 'my_file.txt' not found.")
except PermissionError:
    print("Permission denied to append to file.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
finally:
    print("File appending process completed.\n")
