while True:
    num = int(input("Enter a number: "))

    print(f"Multiplication table for {num}:")
    for i in range(1, 11):
        result = num * i
        print(f"{num} x {1} = {result}")
