def find_value_by_key(dictionary, key):
    return dictionary.get(key, "Not found")


movie_dict = {
    "The Shawshank Redemption": "Frank Darabont",
    "Inception": "Christopher Nolan",
    "Pulp Fiction": "Quentin Tarantino",
    "The Matrix": "Lana Wachowski and Lilly Wachowski"
}


search_key = "Inception"

result = find_value_by_key(movie_dict, search_key)
if result != "Not found":
    print(f"Director of '{search_key}': {result}")
else:
    print(result)
