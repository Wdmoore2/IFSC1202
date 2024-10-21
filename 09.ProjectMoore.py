import csv

def read_csv_to_2d_list(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data

def print_2d_list(data):
    col_widths = [max(len(str(item)) for item in col) for col in zip(*data)]
    for row in data:
        print("  ".join(f"{item:<{col_widths[i]}}" for i, item in enumerate(row)))

def find_city_index(data, city, is_row=True):
    if is_row:
        for i, row in enumerate(data):
            if row[0].strip().lower() == city.strip().lower():
                return i
    else:
        for i, col in enumerate(data[0]):
            if col.strip().lower() == city.strip().lower():
                return i
    return -1

def main():
    filename = '09.Project Distances.csv'
    data = read_csv_to_2d_list(filename)
    
    print("Distance Table:")
    print_2d_list(data)
    
    from_city = input("Enter From City: ").strip()
    to_city = input("Enter To City: ").strip()
    
    from_index = find_city_index(data, from_city, is_row=True)
    to_index = find_city_index(data, to_city, is_row=False)
    
    if from_index == -1:
        print("Invalid From City")
    elif to_index == -1:
        print("Invalid To City")
    else:
        distance = data[from_index][to_index]
        print(from_city,"to",to_city,"-",distance, "Miles")

if __name__ == "__main__":
    main()