# Open the input file for reading and output file for writing
with open('06.04 EmptyLinesInput.txt', 'r') as input_file, open('06.04 EmptyLinesOutput.txt', 'w') as output_file:
    lines_read = 0
    lines_written = 0

    # Read each line from the input file
    for line in input_file:
        lines_read += 1  # Count the line being read
        if line.strip():  # Check if the line is not empty
            output_file.write(line)  # Write the non-empty line to the output file
            lines_written += 1  # Count the line being written

# Print the number of lines read and written
print(f"Number of lines read: {lines_read}")
print(f"Number of lines written: {lines_written}")
