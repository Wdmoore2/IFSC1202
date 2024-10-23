import csv

def read_file_to_2d_list(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = [list(map(int, row[0].split())) for row in reader]
    return data

def swap_columns(data, col1, col2):
    for row in data:
        row[col1], row[col2] = row[col2], row[col1]

def main():
    filename = "09.02 NumbersList.txt"
    try:
        data = read_file_to_2d_list(filename)
    except ValueError:
        print("Error: Non-integer value found in the file.")
        return

    print("Original List:")
    for row in data:
        print(row)

    try:
        i = int(input("Enter the first column number to swap: "))
        j = int(input("Enter the second column number to swap: "))
    except ValueError:
        print("Error: Please enter valid integer column numbers.")
        return

    if not data or not data[0]:
        print("Error: The data is empty or malformed.")
        return

    if 0 <= i < len(data[0]) and 0 <= j < len(data[0]):
        swap_columns(data, i, j)
        print("Modified List:")
        for row in data:
            print(row)
    else:
        print("Error: Column indices are out of range.")

if __name__ == "__main__":
    main()