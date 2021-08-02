def return_10():
    return 10

def add(number_1, number_2):
    return number_1 + number_2

def subtract(number_1, number_2):
    return number_1 - number_2

def multiply(number_1, number_2):
    return number_1 * number_2

def divide(number_1, number_2):
    return number_1 / number_2

def length_of_string(test_string):
    string_length = len(test_string)
    return string_length
def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(string_1, string_2):
    return (int(string_1) + int(string_2))

months = {
    1: "January", 
    2: "February", 
    3: "March", 
    4: "April", 
    5: "May", 
    6: "June", 
    7: "July", 
    8: "August", 
    9: "September", 
    10: "October", 
    11: "November", 
    12: "December", 
    }


def number_to_full_month_name(number):
    return months[number]

def number_to_short_month_name(number):
    return months[number][:3]

def volume_of_cube(side_length):
    return side_length * side_length * side_length

def reverse_string(string):
    return string[::-1]

def temp_converter(fahrenheit):
    return (fahrenheit - 32) / 1.8
