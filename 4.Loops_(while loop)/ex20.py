def sum_of_range(start, end):
    total_sum = 0
    for num in range(start, end + 1):
        total_sum += num
    return total_sum


while True:
    start_num = int(input("Enter the start of the range: "))
    end_num = int(input("Enter the end of the range: "))

    result = sum_of_range(start_num, end_num)
    print("Sum of numbers in the range:", result)
