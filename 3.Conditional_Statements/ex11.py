def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


while True:

    user_year = int(input("Enter a year: "))
    if leap_year(user_year):
        print(user_year, "is a leap year.")
    else:
        print(user_year, "is not a leap year.")
