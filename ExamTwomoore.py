import csv

def read_properties(filename):
    properties = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            row[4] = float(row[4]) 
            properties.append(row) 
    return properties

def print_properties(properties):
    
    headers = ["Address", "City", "State", "Zip Code", "Price"]
    
    col_widths = [max(len(str(item)) for item in col) for col in zip(*properties, headers)]
    
    
    print("  ".join(f"{header:<{col_widths[i]}}" for i, header in enumerate(headers)))
    
    
    print("  ".join("-" * col_widths[i] for i in range(len(headers))))
    
    for row in properties:
        row[4] = f"${row[4]:,.2f}"  
        print("  ".join(f"{str(item):<{col_widths[i]}}" for i, item in enumerate(row)))
    
    print("\nEnd Of All Properties Report")

def process_zipcodes(properties):
    zipcodes = []
    for property in properties:
        zip_code = property[3]
        price = float(property[4].replace('$', '').replace(',', ''))  
        found = False
        for zipcode in zipcodes:
            if zipcode[0] == zip_code:
                zipcode[1] += 1
                zipcode[2] += price
                found = True
                break
        if not found:
            zipcodes.append([zip_code, 1, price])
    return zipcodes

def print_zipcodes_report(zipcodes):
    
    headers = ["Zip Code", "Count of Properties", "Average Property Price"]
    
    
    col_widths = [max(len(str(item)) for item in col) for col in zip(*zipcodes, headers)]
    
    
    print("  ".join(f"{header:<{col_widths[i]}}" for i, header in enumerate(headers)))
    
   
    print("  ".join("-" * col_widths[i] for i in range(len(headers))))
    
    
    for zipcode in zipcodes:
        avg_price = zipcode[2] / zipcode[1]
        formatted_avg_price = f"${avg_price:,.2f}" 
        print(f"{zipcode[0]:<{col_widths[0]}}  {zipcode[1]:<{col_widths[1]}}  {formatted_avg_price:<{col_widths[2]}}")

    print("\n End Of Zip Codes Report")
def main():
    filename = "Exam Two Properties.csv"
    properties = read_properties(filename)
    print("All Properties Report:")
    print_properties(properties)

    zipcodes = process_zipcodes(properties)
    print("\nZip Codes Report:")
    print_zipcodes_report(zipcodes)


if __name__ == "__main__":
    main()