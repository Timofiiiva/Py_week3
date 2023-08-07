def find_union(set1, set2):
    return set1.union(set2)


set1 = {"Lion", "Elephant", "Giraffe", "Tiger", "Monkey"}
set2 = {"Giraffe", "Zebra", "Elephant", "Kangaroo", "Crocodile"}

union_result = find_union(set1, set2)
print("Combined set of animals from both sets:", union_result)
