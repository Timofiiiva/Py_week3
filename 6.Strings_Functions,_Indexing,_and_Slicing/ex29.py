def convert_to_uppercase(input_string):
    return input_string.upper()


while True:
    user_input = input("Enter a string: ")
    uppercase_result = convert_to_uppercase(user_input)
    print("Uppercase string:", uppercase_result)
