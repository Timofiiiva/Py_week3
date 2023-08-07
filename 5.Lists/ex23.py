def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


while True:
    input_list = [int(x) for x in input("Enter a list of numbers separated by \
spaces: ").split()]

    result_list = remove_duplicates(input_list)
    print("List with duplicates removed:", result_list)
