def find_intersection(set1, set2):
    return set1.intersection(set2)


set1 = {"Coding", "Music", "Travel", "Cooking", "Reading"}
set2 = {"Travel", "Photography", "Reading", "Painting", "Gaming"}

intersection_result = find_intersection(set1, set2)
print("Common interests in the two sets:", intersection_result)
