multiples = [ x*7 for x in range(1, 11)]
print(multiples)

languages = ['Python', 'Perl', 'Ruby', 'Go', 'Java', 'C']
lengths = [len(language) for language in languages]
print(lengths)

z = [x for x in range(0, 101) if x % 3 == 0]
print(z)

def odd_numbers(n):
	return [x for x in range(n+1) if x > 0 and x % 2 != 0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []