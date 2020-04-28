def skip_elements(elements):
    # Iniialize variables
    new_list = []
    i = 0

    # Iterate through the list
    for x in elements:
        # Does this element belong in the resulting list?
        if elements.index(x) == i:
            # Add this element to the resulting list
            new_list.append(x)
            # Increment i
            i += 2
    return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']