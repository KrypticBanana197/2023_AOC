def get_first_value(calibration_value):
    for letter in calibration_value:
        if letter.isdigit():
            return letter

def return_total():
    sum_of_calibration_values = 0
    with open('strings.txt', 'r') as file:
        lines = file.read().split()  # Read the file content and split by spaces/newlines
    for value_to_be_calculated in lines:
        sum_of_calibration_values += int(get_first_value(value_to_be_calculated) + get_first_value(value_to_be_calculated[::-1]))
    return sum_of_calibration_values

print(return_total())

### What is the best prefix name for a global variable?
###
### python jokes are awesome