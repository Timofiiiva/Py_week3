def reverse_list(input_list):
    reversed_list = input_list[::-1]
    return reversed_list


while True:
    input_list = input(
        "Enter a list of elements separated by spaces: ").split()

    reversed_result = reverse_list(input_list)
    print("Reversed list:", reversed_result)
