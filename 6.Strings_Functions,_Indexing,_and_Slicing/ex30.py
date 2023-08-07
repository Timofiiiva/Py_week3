def display_first_n_characters(input_string, n):
    return input_string[:n]


while True:
    user_input = input("Enter a string: ")
    n = int(input("Enter the number of characters to display: "))

    result = display_first_n_characters(user_input, n)
    print("First", n, "characters:", result)
