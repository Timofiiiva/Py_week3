def Check_num_in_range(num, lower_limit, upper_limit):
    if lower_limit <= num <= upper_limit:
        return True
    else:
        return False


while True:
    num = float(input("Enter a number: "))
    lower_limit = float(input("Enter the lower limit of the range: "))
    upper_limit = float(input("Enter the upper limit of the range: "))

    if Check_num_in_range(num, lower_limit, upper_limit):
        print("The number is within the specified range.")
    else:
        print("The number is not within the specified range.")
