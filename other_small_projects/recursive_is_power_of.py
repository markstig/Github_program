def is_power_of(number, base):
    if number == base:
        return True
    # if number == 1: # actually, I think we can delete this one. 
        # return True
    if number < base:
        return False
    return is_power_of(number/base, base)

print(is_power_of(8, 2))
print(is_power_of(10, 5))