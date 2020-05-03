# https://www.coursera.org/learn/python-crash-course/supplement/NRd6E/object-composition

class Repository:
    def __init__(self):
        self.packages = {}
    def add_packages(self, package):
        self.packages[package.name] = package
    def total_size(self):
        result = 0
        for package in self.packages.values():
            result += package.size
        return result


# Let’s expand a bit on our Clothing classes from the previous in-video question. Your mission: Finish the "Stock_by_Material" method and iterate over the amount of each item of a given material that is in stock. When you’re finished, the script should add up to 10 cotton Polo shirts.

class Clothing:
    stock = {'name': [], 'material': [], 'amount': []}
    def __init__(self, name):
        material = ''
        self.name = name
    def add_item(self, name, material, amount):
        Clothing.stock['name'].append(self.name)
        Clothing.stock['material'].append(self.material)
        Clothing.stock['amount'].append(amount)
    def Stock_by_Material(self, material):
        count = 0
        n = 0
        for item in Clothing.stock['material']:
            if item == material:
                count += Clothing.stock['amount'][n]
                n+=1
        return count

class shirt(Clothing):
    material = 'Cotton'
class pants(Clothing):
    material = 'Cotton'

polo = shirt('Polo')
sweatpants = pants('Sweatpants')
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
print(Clothing.Stock_by_Material('what', 'Cotton'))