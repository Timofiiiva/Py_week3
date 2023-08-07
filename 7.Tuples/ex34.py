def find_first_occurrence_index(input_tuple, element_to_find):
    try:
        index = input_tuple.index(element_to_find)
        return index
    except ValueError:
        return None


while True:
    input_tuple = tuple(
        input("Enter a tuple of elements separated by spaces: ").split())
    element_to_find = input("Enter the element to find: ")

    index = find_first_occurrence_index(input_tuple, element_to_find)

    if index is not None:
        print(f"The element '{element_to_find}' first occurs at \
index {index}.")
    else:
        print(f"The element '{element_to_find}' is not found in the tuple.")
