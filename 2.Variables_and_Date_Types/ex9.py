while True:
    number = int(input("Enter a number: "))
    number_str = str(number)
    print("Number converted to string:", number_str)

    string_input = input("Enter a string: ")
    if string_input.isnumeric():
        string_to_number = int(string_input)
        print("String converted to number:", string_to_number)
    else:
        print("The input is not a valid numeric string.")
