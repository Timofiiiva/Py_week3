def is_palindrome(input_string):
    return input_string == input_string[::-1]


while True:
    user_input = input("Enter a string: ")
    if is_palindrome(user_input):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
