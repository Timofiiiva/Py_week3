def find_largest_element(input_list):
    largest = input_list[0]
    for num in input_list:
        if num > largest:
            largest = num
    return largest


while True:
    input_list = [int(x) for x in input("Enter a list of number\
 separated by spaces: ").split()]

    largest_element = find_largest_element(input_list)
    print("Largest element in the list:", largest_element)
