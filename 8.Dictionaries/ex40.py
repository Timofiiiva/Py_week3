def combine_dictionaries(dict1, dict2):
    combined_dict = {}
    for key in dict1:
        combined_dict[key] = [dict1[key], dict2.get(key, "N/A")]
    for key in dict2:
        if key not in dict1:
            combined_dict[key] = ["N/A", dict2[key]]
    return combined_dict


scientist_birth_dict = {
    "Albert Einstein": 1879,
    "Marie Curie": 1867,
    "Isaac Newton": 1643,
    "Charles Darwin": 1809
}

scientist_field_dict = {
    "Albert Einstein": "Theoretical Physics",
    "Marie Curie": "Physics and Chemistry",
    "Galileo Galilei": "Physics and Astronomy",
    "Nikola Tesla": "Electrical Engineering"
}

combined = combine_dictionaries(scientist_birth_dict, scientist_field_dict)
print("Combined dictionary:")
for key, values in combined.items():
    birth_year, field = values
    print(f"{key}: Birth Year - {birth_year}, Field - {field}")
