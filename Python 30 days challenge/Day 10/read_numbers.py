# Step 1: Create the file (only needed once)
with open("numbers.txt", "w") as f:
    f.write("10\n20.5\nabc\n30\n-15\nxyz\n")

# Step 2: Function to read numbers and collect invalid entries
def read_numbers_from_file(filename):
    numbers_list = []
    invalid_texts_list = []

    try:
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                try:
                    number = float(line)
                    numbers_list.append(number)
                except ValueError:
                    print(f"⚠️ Warning: Invalid number on line {line_number}: '{line}'")
                    invalid_texts_list.append(line)

    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"❗ An unexpected error occurred: {e}")
    finally:
        print("📄 File reading operation completed.")  # This always runs

    return numbers_list, invalid_texts_list

# Example usage
file_path = 'numbers.txt'
valid_numbers, invalid_texts = read_numbers_from_file(file_path)

print("Valid numbers:", valid_numbers)
print("Invalid text entries:", invalid_texts)
