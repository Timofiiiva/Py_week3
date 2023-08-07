def check_subset(set1, set2):
    return set1.issubset(set2)


set1 = {"Programming", "Problem Solving", "Teamwork"}
set2 = {"Programming", "Problem Solving",
        "Communication", "Teamwork", "Leadership"}

is_subset = check_subset(set1, set2)

if is_subset:
    print("Set 1's skills are a subset of Set 2's skills.")
else:
    print("Set 1's skills are not a subset of Set 2's skills.")
