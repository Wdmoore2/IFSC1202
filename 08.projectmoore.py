def read_constitution(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

def find_section(lines, search_term):
    results = []
    for i, line in enumerate(lines):
        if search_term.lower() in line.lower():
            start = i
            end = i
            while start > 0 and lines[start - 1] != '':
                start -= 1
            while end < len(lines) - 1 and lines[end + 1] != '':
                end += 1
            results.append((start, end))
    return results

def display_sections(lines, sections):
    for start, end in sections:
        print(f"Section starting at line {start + 1}:")
        for i in range(start, end + 1):
            print(lines[i])
        print("\n" + "-"*40 + "\n")

def main():
    file_path = 'constitution.txt'
    lines = read_constitution(file_path)
    
    while True:
        search_term = input("Enter a search term (or press Enter to exit): ").strip()
        if not search_term:
            break
        sections = find_section(lines, search_term)
        if sections:
            display_sections(lines, sections)
        else:
            print("No sections found containing the search term.")

if __name__ == "__main__":
    main()