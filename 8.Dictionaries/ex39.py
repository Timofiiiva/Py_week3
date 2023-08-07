def check_key_exists(dictionary, key):
    return key in dictionary


language_creator_dict = {
    "Python": "Guido van Rossum",
    "Java": "James Gosling",
    "C++": "Bjarne Stroustrup",
    "JavaScript": "Brendan Eich"
}


check_key = "Python"

if check_key_exists(language_creator_dict, check_key):
    print(f"The key '{check_key}' exists in the dictionary.")
else:
    print(f"The key '{check_key}' does not exist in the dictionary.")
