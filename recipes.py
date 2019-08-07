allRecipes = {}

class Recipe():

    def __init__(self, name, building, rate, ingredients={}):
        self.name = name
        self.building = building
        self.rate = rate
        self.ingredients = ingredients
        allRecipes[name] = self




Recipe('Screws', 'Constructor', '60', {'Iron Bars':1})
Recipe('Iron Ore', 'Miner', '120')

print(allRecipes)