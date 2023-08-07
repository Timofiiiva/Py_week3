def combine_tuples(tuple1, tuple2):
    combined_tuple = tuple1 + tuple2
    return combined_tuple


while True:
    tuple1 = tuple(
        input("Enter the first tuple elements separated by spaces: ").split())
    tuple2 = tuple(
        input("Enter the second tuple elements separated by spaces: ").split())

    result_tuple = combine_tuples(tuple1, tuple2)
    print("Combined tuple:", result_tuple)
