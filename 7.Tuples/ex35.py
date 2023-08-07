def is_empty_tuple(input_tuple):
    return len(input_tuple) == 0


while True:
    input_tuple = tuple(
        input("Enter a tuple of elements separated by spaces: ").split())

    if is_empty_tuple(input_tuple):
        print("The tuple is empty.")
    else:
        print("The tuple is not empty.")
