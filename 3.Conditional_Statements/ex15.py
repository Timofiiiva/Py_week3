def find_smaller_num(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2


while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    smaller_num = find_smaller_num(num1, num2)
    print(f"The smaller number is: {smaller_num}")
