def remove_element(set_, element):
    if element in set_:
        set_.remove(element)
        return True
    else:
        return False


mythical_creatures = {"Dragon", "Phoenix", "Unicorn", "Kraken", "Sphinx"}


remove_mythical_creature = "Unicorn"

if remove_element(mythical_creatures, remove_mythical_creature):
    print(
        f"The {remove_mythical_creature} has vanished from the realm of \
mythical creatures.")
else:
    print(
        f"The {remove_mythical_creature} wasn't found among the mythical \
creatures.")

print("Remaining mythical creatures:", mythical_creatures)
