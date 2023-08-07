def remove_extra_spaces(input_string):
    return ' '.join(input_string.split())


while True:
    user_input = input("Enter a string with extra spaces: ")
    result = remove_extra_spaces(user_input)
    print("String with extra spaces removed:", result)
