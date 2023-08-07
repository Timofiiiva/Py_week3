def sum_of_tuple_elements(input_tuple):
    total_sum = sum(input_tuple)
    return total_sum


while True:
    input_tuple = tuple(
        map(int, input("Enter a tuple of numbers separated by \
spaces: ").split()))

    result = sum_of_tuple_elements(input_tuple)
    print("Sum of elements in the tuple:", result)
