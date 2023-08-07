def sum_of_list_elements(input_list):
    total_sum = sum(input_list)
    return total_sum


while True:
    input_list = [int(x) for x in input("Enter a list of numbers separated by \
spaces: ").split()]

    result = sum_of_list_elements(input_list)
    print("Sum of elements in the list:", result)
