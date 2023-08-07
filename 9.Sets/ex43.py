def find_symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)


set1 = {"Reading", "Hiking", "Cooking", "Photography", "Painting"}
set2 = {"Hiking", "Gaming", "Travelling", "Music", "Cooking"}

symmetric_difference_result = find_symmetric_difference(set1, set2)
print("Hobbies unique to each set:", symmetric_difference_result)
