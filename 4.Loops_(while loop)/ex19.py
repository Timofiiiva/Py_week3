def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


while True:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    result = gcd(num1, num2)
    print("Greatest Common Divisor:", result)
