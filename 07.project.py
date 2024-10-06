import re

def ParseDegreeString(degree_string):
    pattern = r"(\d+)°(\d+)'(\d+(\.\d+)?)\""
    match = re.match(pattern, degree_string)
    degrees = int(match.group(1))
    minutes = int(match.group(2))
    seconds = float(match.group(3))
    return degrees, minutes, seconds

def DDMMSStoDecimal(degrees, minutes, seconds):
    decimal_degrees = degrees + (minutes / 60) + (seconds / 3600)
    return decimal_degrees

def convert_angles(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    results = []
    for line in lines:
        line = line.strip()
        if line:
            degrees, minutes, seconds = ParseDegreeString(line)
            decimal_degrees = DDMMSStoDecimal(degrees, minutes, seconds)
            results.append(decimal_degrees)

    with open(output_file, 'w') as outfile:
        for result in results:
            outfile.write(f"{result}\n")

    print(f"{len(results)} Records Processed")

input_file = '07.Project Angles Input.txt'
output_file = '07.Project Angles Output.txt'
convert_angles(input_file, output_file)