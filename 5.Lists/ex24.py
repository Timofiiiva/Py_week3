def average_of_list_elements(input_list):
    total_sum = sum(input_list)
    num_elements = len(input_list)
    if num_elements == 0:
        return 0
    average = total_sum / num_elements
    return average


while True:
    input_list = [int(x) for x in input("Enter a list of numbers separated by \
spaces: ").split()]

    average_value = average_of_list_elements(input_list)
    print("Average value of elements in the list:", average_value)
