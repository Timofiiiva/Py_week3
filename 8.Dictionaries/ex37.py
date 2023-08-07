def calculate_sum_of_values(dictionary):
    return sum(dictionary.values())


num_dict = {"a": 39, "b": 21, "c": 36, "d": 4}

total_sum = calculate_sum_of_values(num_dict)
print(f"The sum of all values in the dictionary is: {total_sum}")
