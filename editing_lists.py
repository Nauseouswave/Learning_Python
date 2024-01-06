
supplies = ["tent", "sleeping bags", "water", "raspberry pi", "coffee", "knife", "ethernet cable", "flash drive", "bread dough", "honey butter"]


camp_site = ["Crystal Lake", 404, 89.3, True]

# Ways to add to lists

# Add one item
supplies.append("bidet")

# Add a list
supplies.extend(["tissues", "matches"])

# Add list to a list
supplies = supplies + ["MRE's", "water"]

# Adds to the list by index (0 = first item in list)
supplies.insert(0, "Axe")
supplies.insert(-1, "toilet paper")

# Ways to remove from a list

# Deletes whole list
# supplies.clear()

# Remove one piece of data from a list
# supplies.remove("tent")
# supplies.remove("sleeping bags")

# Removes second item in list (tent)
supplies.pop(1)

# Removes new second item in list (sleeping bags)
print("This item was just deleted: " + supplies.pop(1))


print(supplies)
