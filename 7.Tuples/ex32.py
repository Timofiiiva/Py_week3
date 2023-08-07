def find_largest_element(input_tuple):
    return max(input_tuple)


while True:
    input_tuple = tuple(
        map(int, input("Enter a tuple of numbers separated by \
spaces: ").split()))

    largest_element = find_largest_element(input_tuple)
    print("Largest element in the tuple:", largest_element)
