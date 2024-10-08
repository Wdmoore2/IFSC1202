start_range = int(input("Enter start of range: ")) 
end_range = int(input("Enter end of range: "))
def find_special_numbers(start, end):
    special_numbers = []
    for number in range(start, end + 1):
        original_number = number
        temp_number = number
        digit_count = 0

        while temp_number > 0:
            temp_number //= 10
            digit_count += 1

        temp_number = original_number
        sum_of_powers = 0

        while temp_number > 0:
            digit = temp_number % 10
            sum_of_powers += digit ** digit_count
            temp_number //= 10

        if sum_of_powers == original_number:
            special_numbers += [original_number]
    
    return special_numbers
special_numbers = find_special_numbers(start_range, end_range)
print(special_numbers)