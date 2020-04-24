def sum_positive_number(n):
    if n < 1:
        return 0
    return n + sum_positive_number(n-1)

print(sum_positive_number(3))
print(sum_positive_number(6))
