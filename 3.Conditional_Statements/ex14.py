def check_vowel_or_consonant(character):
    vowel = "aeiouAEIOU"

    if character.isalpha():
        if character in vowel:
            return f"{character} is a vowel."
        else:
            return f"{character} is a consonant."
    else:
        return "Invalid input. Please enter an alphabetical character."


while True:
    user_input = input("Enter a character: ")
    result = check_vowel_or_consonant(user_input)
    print(result)
