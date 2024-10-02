def merge_files(input_file, merge_file, output_file):
    input_record_count = 0
    merge_record_count = 0
    output_record_count = 0
    
    with open(output_file, 'w') as output:
        with open(input_file, 'r') as input:
            for line in input:
                if '**Insert Merge File Here**' in line:
                    with open(merge_file, 'r') as merge:
                        for merge_line in merge:
                            output.write(merge_line.strip()+'\n')
                            merge_record_count += 1
                            output_record_count += 1
                else:
                    output.write(line)
                    input_record_count += 1
                    output_record_count += 1

    print(f"{input_record_count} input file records")
    print(f"{merge_record_count} merge file records")
    print(f"{output_record_count} output file records")

input_file = '06.Project Input File.txt'
merge_file = '06.Project Merge File.txt'
output_file = '06.Project Output File.txt'
merge_files(input_file, merge_file, output_file)