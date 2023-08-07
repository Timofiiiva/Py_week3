def remove_element_by_key(dictionary, key):
    if key in dictionary:
        removed_value = dictionary.pop(key)
        return removed_value
    else:
        return "Key not found"


landmark_dict = {
    "Eiffel Tower": "Iconic iron lattice tower in Paris.",
    "Great Wall of China": "Long wall built along northern borders of China.",
    "Statue of Liberty": "Giant neoclassical statue in New York Harbor.",
    "Taj Mahal": "White marble mausoleum in Agra, India."
}


remove_key = "Statue of Liberty"

removed_value = remove_element_by_key(landmark_dict, remove_key)
if removed_value != "Key not found":
    print(
        f"Information about '{remove_key}': '{removed_value}' has been \
removed.")
else:
    print(f"Key '{remove_key}' not found in the dictionary.")

print("Updated dictionary:", landmark_dict)
