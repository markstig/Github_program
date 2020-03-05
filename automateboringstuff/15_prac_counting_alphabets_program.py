# Character Counting Program Example
import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

count = {}

for character in message.upper():
    count.setdefault(character,
                     0)  # add a key in the dic if there is no such key
    count[character] = count[
        character] + 1  # count the number of th key, if the key already existed, they the key value added one.

pprint.pprint(count)

rjtext = pprint.pformat(count)
print(rjtext)

list1 = {}
list1.setdefault('a', 1)
list1.setdefault('a', 2)
print(list1)
