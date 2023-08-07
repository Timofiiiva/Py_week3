def count_substring_occurrences(main_string, substring):
    return main_string.count(substring)


while True:
    main_string = input("Enter a main string: ")
    substring = input("Enter a substring to count: ")

    occurrences = count_substring_occurrences(main_string, substring)
    print(
        f"The substring '{substring}' appears {occurrences} times in the \
main string.")
