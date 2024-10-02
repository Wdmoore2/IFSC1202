def FahrToCel(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9

# Open the Fahrenheit temperatures file for reading
with open('06.03 FTemps.txt', 'r') as f_in, open('06.03 CTemps.txt', 'w') as f_out:
    records_processed = 0

    # Read and process each line
    for line in f_in:
        fahrenheit_temp = float(line.strip())
        celsius_temp = FahrToCel(fahrenheit_temp)

        # Write the Celsius temperature to the output file
        f_out.write(f"{celsius_temp:5.1f}\n")
        
        # Increment the count of records processed
        records_processed += 1

# Print the number of records processed
print(f"Number of records processed: {records_processed}")
