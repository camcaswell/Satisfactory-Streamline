allRecipes = {}

class Recipe():

    def __init__(self, name, variant, building, rate, count, ingredients):
        self.name = name
        self.variant = variant
        self.building = building
        self.rate = rate #Per Minute
        self.count = count #Per Operation
        self.ingredients = ingredients #Per Operation
        allRecipes[name] = self

#Tier 0 Components
#Recip('Name',					'Variant',		'Machine',		'Rate', 'Count',{'Ingredient':1})
Recipe('Biomass',				'Leaves',		'Constructor',	'90',	'6',	{'Leaves':10})
Recipe('Biomass',				'Wood',			'Constructor',	'375',	'25',	{'Wood':5})
Recipe('Cable',					'Default',		'Constructor',	'15',	'1',	{'Wire':2})
Recipe('Cable',					'Rubber',		'Assembler',	'75',	'10',	{'Wire':3, 'Rubber':2})
Recipe('Concrete',				'Default',		'Constructor',	'15',	'1',	{'Limestone':3})
Recipe('Concrete',				'Alternate',	'Assembler',	'22.5',	'3',	{'Silica':1, 'Limestone':4})
Recipe('Copper Ingot',			'Default',		'Smelter',		'30',	'1',	{'Copper Ore':1})
Recipe('Iron Ingot',			'Default',		'Smelter',		'30',	'1',	{'Iron Ore':1})
Recipe('Iron Ingot',			'Alloy',		'Foundry',		'45',	'3',	{'Iron Ore':1, 'Copper Ore':1})
Recipe('Iron Plate',			'Default',		'Constructor',	'15',	'1',	{'Iron Ingot':2})
Recipe('Iron Rod',				'Default',		'Constructor',	'15',	'1',	{'Iron Ingot':1})
Recipe('Reinforced Iron Plate',	'Default',		'Assembler',	'5',	'1',	{'Iron Plate':4, 'Screw':24})
Recipe('Reinforced Iron Plate',	'Alternate',	'Assembler',	'7.5',	'3',	{'Iron Plate':10, 'Screw':24})
Recipe('Reinforced Iron Plate',	'Stitched',		'Assembler',	'7.5',	'3',	{'Iron Plate':6, 'Wire':30})
Recipe('Screw',					'Default',		'Constructor',	'90',	'6',	{'Iron Rod':1})
Recipe('Screw',					'Alternate',	'Constructor',	'90',	'12',	{'Iron Ingot':2})
Recipe('Screw',					'Steel',		'Constructor',	'180',	'36',	{'Steel Beam':1})
Recipe('Wire',					'Default',		'Constructor',	'45',	'3',	{'Copper Ingot':1})
Recipe('Wire',					'Iron',			'Constructor',	'67.5',	'9',	{'Iron Ingot':2})
Recipe('Wire',					'Caterium',		'Constructor',	'67.5',	'9',	{'Caterium Ingot':1})

#Tier 1 Components
#Recip('Name',			'Variant',	'Machine',		'Rate', 'Count',{'Ingredient':1})
Recipe('Biomass',		'Mycelia',	'Constructor',	'150',	'10',	{'Mycelia':10})
Recipe('Biofuel',		'Default',	'Constructor',	'30',	'2',	{'Biomass':4})
Recipe('Fabric',		'Default',	'Assembler',	'15',	'1',	{'Mycelia':1, 'Biomass':5})
Recipe('Power Shard',	'Green',	'Constructor',	'6',	'1',	{'Green Power Slug':1})
Recipe('Power Shard',	'Yellow',	'Constructor',	'8',	'2',	{'Yellow Power Slug':1})
Recipe('Power Shard',	'Purple',	'Constructor',	'15',	'5',	{'Purple Power Slug':1})

#Tier 2 Components
#Recip('Name',			'Variant',		'Machine',		'Rate', 'Count',{'Ingredient':1})
Recipe('Modular Frame',	'Default',		'Assembler',	'4',	'1',	{'Reinforced Iron Plate':3, 'Iron Rod':6})
Recipe('Modular Frame',	'Alternate',	'Assembler',	'6',	'3',	{'Reinforced Iron Plate':6, 'Steel Pipe':6})
Recipe('Rotor',			'Default',		'Assembler',	'6',	'1',	{'Iron Rod':3, 'Screw':22})
Recipe('Rotor',			'Alternate',	'Assembler',	'9',	'3',	{'Steel Pipe':6, 'Wire':20})

#Tier 3 Components
#Recip('Name',				'Variant',			'Machine',		'Rate', 'Count',{'Ingredient':1})
Recipe('Biomass',			'Alien Carapace',	'Constructor',	'1500',	'100',	{'Alien Carapace':1})
Recipe('Caterium Ingot',	'Default',			'Smelter',		'15',	'1',	{'Caterium Ore':3})
Recipe('Quickwire',			'Default',			'Constructor',	'60',	'4',	{'Caterium Ingot':1})
Recipe('Quickwire',			'Alternate',		'Constructor',	'90',	'12',	{'Caterium Ingot':1, 'Copper Ingot':2})

#Tier 4 Components
#Recip('Name',			'Variant',			'Machine',		'Rate', 'Count',{'Ingredient':1})



print(allRecipes)