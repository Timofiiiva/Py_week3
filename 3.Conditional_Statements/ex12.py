def check_even_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"


while True:
    input_num = int(input("Enter a number: "))
    result = check_even_odd(input_num)
    print(input_num, "is", result)
