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
Recipe('Quickwire',			'Alternate',		'Assembler',	'90',	'12',	{'Caterium Ingot':1, 'Copper Ingot':2})

#Tier 4 Components
#Recip('Name',						'Variant',		'Machine',		'Rate', 'Count',{'Ingredient':1})
Recipe('Black Powder',				'Default',		'Assembler',	'7.5',	'1',	{'Coal':1, 'Sulfur':2})
Recipe('Black Powder',				'Alternate',	'Assembler',	'15',	'4',	{'Compacted Coal':1, 'Sulfur':2})
Recipe('Compacted Coal',			'Default',		'Assembler',	'30',	'3',	{'Coal':3, 'Sulfur':3})
Recipe('Crystal Oscillator',		'Default',		'Manufacturer',	'1.9',	'1',	{'Quartz Crystal':10, 'Cable':14, 'Reinforced Iron Plate':4})
Recipe('Crystal Oscillator',		'Alternate',	'Manufacturer',	'2.8',	'3',	{'Quartz Crystal':20, 'Rubber':24, 'A.I. Limiter':1})
Recipe('Encased Industrial Beam',	'Default',		'Assembler',	'4',	'1',	{'Steel Beam':4, 'Concrete':5})
Recipe('Encased Industrial Beam',	'Alternate',	'Assembler',	'6',	'3',	{'Steel Pipe':18, 'Concrete':10})
Recipe('Heavy Modular Frame',		'Default',		'Manufacturer',	'2',	'1',	{'Modular Frame':5, 'Steel Pipe':15, 'Encased Industrial Beam':5, 'Screw':90})
Recipe('Heavy Modular Frame',		'Alternate',	'Manufacturer',	'2.8',	'3',	{'Modular Frame':8, 'Steel Pipe':36, 'Encased Industrial Beam':10, 'Concrete':25})
Recipe('Motor',						'Default',		'Assembler',	'5',	'1',	{'Rotor':2, 'Stator':2})
Recipe('Motor',						'Alternate',	'Manufacturer',	'7.5',	'3',	{'Rotor':2, 'Stator':2, 'Crystal Oscillator':1})
Recipe('Quartz Crystal',			'Default',		'Constructor',	'15',	'1',	{'Raw Quartz':2})
Recipe('Silica',					'Default',		'Constructor',	'45',	'3',	{'Raw Quartz':3})
Recipe('Silica',					'Alternate',	'Assembler',	'67.5',	'9',	{'Raw Quartz':4, 'Limestone':2})
Recipe('Stator',					'Default',		'Assembler',	'6',	'1',	{'Steel Pipe':3, 'Wire':10})
Recipe('Stator',					'Alternate',	'Assembler',	'9',	'3',	{'Steel Pipe':6, 'Quickwire':20})
Recipe('Steel Beam',				'Default',		'Constructor',	'10',	'1',	{'Steel Ingot':3})
Recipe('Steel Ingot',				'Default',		'Foundry',		'30',	'2',	{'Iron Ore':3, 'Coal':3})
Recipe('Steel Ingot',				'Enriched',		'Foundry',		'45',	'6',	{'Iron Ore':6, 'Compacted Coal':3})
Recipe('Steel Ingot',				'Alternate',	'Foundry',		'45',	'6',	{'Iron Ingot':3, 'Coal':6})
Recipe('Steel Pipe',				'Default',		'Constructor',	'15',	'1',	{'Steel Ingot':1})

#Tier 5 Components
#Recip('Name',					'Variant',		'Machine',		'Rate', 'Count',{'Ingredient':1})
Recipe('A.I. Limiter',			'Default',		'Assembler',	'5',	'1',	{'Circuit Board':2, 'Quickwire':18})
Recipe('Circuit Board',			'Default',		'Assembler',	'10',	'2',	{'Wire':12, 'Plastic':6})
Recipe('Circuit Board',			'Alternate',	'Assembler',	'15',	'6',	{'Wire':24, 'Rubber':16})
Recipe('Circuit Board',			'Quickwire',	'Assembler',	'15',	'6',	{'Quickwire':30, 'Plastic':12})
Recipe('Computer',				'Default',		'Manufacturer',	'1.9',	'1',	{'Circuit Board':10, 'Cable':12, 'Plastic':18, 'Screw':60})
Recipe('Computer',				'Crystal',		'Assembler',	'2.5',	'1',	{'Circuit Board':4, 'Crystal Oscillator':1})
Recipe('Computer',				'Quickwire',	'Manufacturer',	'2.8',	'3',	{'Circuit Board':20, 'Quickwire':80, 'Rubber':48})
Recipe('Fuel',					'Default',		'Oil Refinery',	'37.5',	'5',	{'Crude Oil':8})
Recipe('High-Speed Connector',	'Default',		'Manufacturer',	'2.5',	'1',	{'Quickwire':40, 'Cable':10, 'Plastic':6})
Recipe('High-Speed Connector',	'Alternate',	'Manufacturer',	'3.8',	'3',	{'Quickwire':66, 'Silica':48, 'Rubber':18})
Recipe('Plastic',				'Default',		'Refinery',		'22.5',	'3',	{'Crude Oil':4})
Recipe('Plastic',				'Alternate',	'Assembler',	'33.8',	'9',	{'Rubber':8, 'Fuel':5})
Recipe('Rubber',				'Default',		'Oil Refinery',	'30',	'4',	{'Crude Oil':4})
Recipe('Supercomputer',			'Default',		'Manufacturer',	'1.9',	'1',	{'Computer':2, 'A.I. Limiter':2, 'High-Speed Connector':3, 'Plastic':21})

#Tier 6 Components
#Recip('Name',		'Variant',	'Machine',		'Rate', 'Count',{'Ingredient':1})
Recipe('TURBOFUEL',	'Default',	'Assembler',	'18.8',	'5',	{'Fuel':5, 'Compacted Coal':4})

#Tier 7 Components
#Recip('Name',							'Variant',		'Machine',				'Rate', 'Count',{'Ingredient':1})
Recipe('Alclad Aluminum Sheet',			'Default',		'Assembler',			'15',	'3',	{'Aluminum Ingot':3, 'Copper Ingot':2})
Recipe('Aluminum Ingot',				'Default',		'Foundry',				'30',	'2',	{'Bauxite':7, 'Silica':6})
Recipe('Battery',						'Default',		'Manufacturer',			'5.6',	'3',	{'Alclad Aluminum Sheet':8, 'Wire':24, 'Sulfur':20, 'Plastic':9})
Recipe('Electromagnetic Control Rod',	'Default',		'Assembler',			'2',	'1',	{'Stator':3, 'A.I. Limiter':2})
Recipe('Electromagnetic Control Rod',	'Alternate',	'Assembler',			'3',	'3',	{'Stator':6, 'High-Speed Connector':3})
Recipe('Heat Sink',						'Default',		'Assembler',			'5',	'1',	{'Alclad Aluminum Sheet':4, 'Rubber':10})
Recipe('Heat Sink',						'Alternate',	'Assembler',			'7.5',	'3',	{'Alclad Aluminum Sheet':8, 'Wire':36})
Recipe('Nuclear Fuel Rod',				'Default',		'Manufacturer',			'0.4',	'1',	{'Uranium Cell':25, 'Encased Industrial Beam':3, 'Electromagnetic Control Rod':5})
Recipe('Nuclear Fuel Rod',				'Alternate',	'Manufacturer',			'0.6',	'3',	{'Uranium Cell':50, 'Electromagnetic Control Rod':10, 'Crystal Oscillator':3, 'Beacon':6})
Recipe('Nuclear Waste',					'Default',		'Nuclear Power Plant',	'5',	'25',	{'Nuclear Fuel Rod':1})
Recipe('Radio Control Unit',			'Default',		'Manufacturer',			'2.5',	'1',	{'Heat Sink':4, 'Rubber':24, 'Crystal Oscillator':1, 'Computer':1})
Recipe('Radio Control Unit',			'Alternate',	'Manufacturer',			'3.8',	'3',	{'Heat Sink':10, 'Quartz Crystal':30, 'Supercomputer':1})
Recipe('TURBO MOTOR',					'Default',		'Manufacturer',			'1.9',	'1',	{'Heat Sink':4, 'Radio Control Unit':2, 'Motor':4, 'Rubber':40})
Recipe('TURBO MOTOR',					'Alternate',	'Manufacturer',			'2.8',	'3',	{'Motor':8, 'Radio Control Unit':4, 'A.I. Limiter':8, 'Stator':8})
Recipe('Uranium Cell',					'Default',		'Assembler',			'10',	'10',	{'Uranium':45, 'Concrete':9})
Recipe('Uranium Cell',					'Alternate',	'Manufacturer',			'17.5',	'35',	{'Uranium':45, 'Sulfur':45, 'Silica':45, 'Quickwire':60})

#Tier 0 Tools
#Recip('Name',				'Variant',		'Machine',						'Rate', 'Count',{'Ingredient':1})
Recipe('Beacon',			'Default',		'Manufacturer',					'7.5',	'1',	{'Iron Plate':3, 'Iron Rod':1, 'Wire':15, 'Cable':2})
Recipe('Beacon',			'Alternate',	'Manufacturer',					'9.4',	'5',	{'Steel Beam':1, 'Steel Pipe':4, 'Crystal Oscillator':1})
Recipe('Object Scanner',	'Default',		'Equipment Workshop (Manual)',	'1.5',	'1',	{'Reinforced Iron Plate':4, 'Beacon':3, 'Screw':50})
Recipe('Portable Miner',	'Default',		'Equipment Workshop (Manual)',	'1.5',	'1',	{'Iron Plate':4, 'Wire':8, 'Cable':4})
Recipe('Xeno-Zapper',		'Default',		'Equipment Workshop (Manual)',	'1.5',	'1',	{'Iron Rod':10, 'Reinforced Iron Plate':2, 'Cable':15, 'Wire':50})

#Tier 1 Tools
#Recip('Name',	'Variant',	'Machine',	'Rate', 'Count',{'Ingredient':1})

#Tier 2 Tools
#Recip('Name',				'Variant',	'Machine',						'Rate', 'Count',{'Ingredient':1})
Recipe('Chainsaw',			'Default',	'Equipment Workshop (Manual)',	'1',	'1',	{'Reinforced Iron Plate':10, 'Iron Rod':25, 'Screw':160, 'Cable':15})
Recipe('Color Gun',			'Default',	'Equipment Workshop (Manual)',	'0.75',	'1',	{'Iron Plate':5, 'Screw':80, 'Wire':40})
Recipe('Color Cartridge',	'Default',	'Constructor',					'75',	'50',	{'Flower Petals':25})
Recipe('Parachute',			'Default',	'Equipment Workshop (Manual)',	'7.5',	'5',	{'Fabric':10, 'Cable':5})

#Tier 3 Tools
#Recip('Name',				'Variant',		'Machine',						'Rate', 'Count',{'Ingredient':1})
Recipe('Blade Runners',		'Default',		'Equipment Workshop (Manual)',	'0.75',	'1',	{'Quickwire':50, 'Modular Frame':3, 'Rotor':3})
Recipe('Medicinal Inhaler',	'Default',		'Equipment Workshop (Manual)',	'3',	'1',	{'Bacon Agaric':1, 'Paleberry':2, 'Beryl Nut':3, 'Mycelia':5})
Recipe('Medicinal Inhaler',	'Alien Organs',	'Equipment Workshop (Manual)',	'3',	'1',	{'Alien Organs':3, 'Mycelia':5})
Recipe('Rebar Gun',			'Default',		'Equipment Workshop (Manual)',	'0.6',	'1',	{'Reinforced Iron Plate':6, 'Iron Rod':16, 'Screw':100})
Recipe('Spiked Rebar',		'Default',		'Constructor',					'15',	'1',	{'Iron Rod':1})

#Tier 4 Tools
#Recip('Name',					'Variant',		'Machine',						'Rate', 'Count',{'Ingredient':1})
Recipe('Nobelisk Detonator',	'Default',		'Equipment Workshop (Manual)',	'0.75',	'1',	{'Object Scanner':5, 'Encased Industrial Beam':10, 'Cable':50})
Recipe('Nobelisk',				'Default',		'Manufacturer',					'3',	'1',	{'Black Powder':5, 'Steel Pipe':5, 'Beacon':1})
Recipe('Nobelisk',				'Alternate',	'Manufacturer',					'4.5',	'3',	{'Black Powder':10, 'Steel Pipe':10, 'Crystal Oscillator':1})
Recipe('Xeno-Basher',			'Default',		'Equipment Workshop (Manual)',	'0.75',	'1',	{'Modular Frame':5, 'Xeno-Zapper':2, 'Cable':25, 'Wire':500})

#Tier 5 Tools
#Recip('Name',		'Variant',	'Machine',						'Rate', 'Count',{'Ingredient':1})
Recipe('Rifle',		'Default',	'Equipment Workshop (Manual)',	'0.5',	'1',	{'Steel Pipe':25, 'Heavy Modular Frame':3, 'Circuit Board':20, 'Screw':250})
Recipe('Cartridge',	'Default',	'Assembler',					'12',	'4',	{'Nobelisk':1, 'Steel Pipe':4})

#Tier 6 Tools
#Recip('Name',		'Variant',	'Machine',						'Rate', 'Count',{'Ingredient':1})
Recipe('Gas Mask',	'Default',	'Equipment Workshop (Manual)',	'0.75',	'1',	{'Rubber':100, 'Plastic':100, 'Fabric':100})
Recipe('Filter',	'Default',	'Manufacturer',					'7.5',	'1',	{'Coal':5, 'Rubber':2, 'Fabric':2})
Recipe('Jetpack',	'Default',	'Equipment Workshop (Manual)',	'0.5',	'1',	{'Plastic':50, 'Circuit Board':15, 'Rubber':50, 'Cable':25})

#Tier 7 Tools
#Recip('Name',					'Variant',	'Machine',						'Rate', 'Count',{'Ingredient':1})
Recipe('Hazmat Suit',			'Default',	'Equipment Workshop (Manual)',	'0.5',	'1',	{'Rubber':50, 'Plastic':50, 'Alclad Aluminum Plate':50, 'Fabric':50})
Recipe('Iodine Infused Filter',	'Default',	'Manufacturer',					'3.75',	'1',	{'Filter':1, 'Quickwire':8,	'Rubber':2})

#Resources Ores
#Recip('Name',		'Variant',	'Machine',		'Rate', 'Count',{'Ingredient':1})
Recipe('Bauxite',		'Impure',	'Miner MK3',	'120',	'1',	{})
Recipe('Bauxite',		'Normal',	'Miner MK3',	'240',	'1',	{})
Recipe('Bauxite',		'Pure',		'Miner MK3',	'480',	'1',	{}) #Max Output Capped by Belt MK5
#Recipe('Caterium Ore',	'Impure',	'Miner MK3',	'120',	'1',	{}) #None In Game
Recipe('Caterium Ore',	'Normal',	'Miner MK3',	'240',	'1',	{})
Recipe('Caterium Ore',	'Pure',		'Miner MK3',	'480',	'1',	{}) #Max Output Capped by Belt MK5
Recipe('Coal',			'Impure',	'Miner MK3',	'120',	'1',	{})
Recipe('Coal',			'Normal',	'Miner MK3',	'240',	'1',	{})
Recipe('Coal',			'Pure',		'Miner MK3',	'480',	'1',	{}) #Max Output Capped by Belt MK5
Recipe('Copper Ore',	'Impure',	'Miner MK3',	'120',	'1',	{})
Recipe('Copper Ore',	'Normal',	'Miner MK3',	'240',	'1',	{})
Recipe('Copper Ore',	'Pure',		'Miner MK3',	'480',	'1',	{}) #Max Output Capped by Belt MK5
Recipe('Crude Oil',		'Impure',	'Oil Pump MK1',	'120',	'1',	{})
Recipe('Crude Oil',		'Normal',	'Oil Pump MK1',	'240',	'1',	{})
Recipe('Crude Oil',		'Pure',		'Oil Pump MK1',	'480',	'1',	{})
Recipe('Iron Ore',		'Impure',	'Miner MK3',	'120',	'1',	{})
Recipe('Iron Ore',		'Normal',	'Miner MK3',	'240',	'1',	{})
Recipe('Iron Ore',		'Pure',		'Miner MK3',	'480',	'1',	{}) #Max Output Capped by Belt MK5
Recipe('Limestone',		'Impure',	'Miner MK3',	'120',	'1',	{})
Recipe('Limestone',		'Normal',	'Miner MK3',	'240',	'1',	{})
Recipe('Limestone',		'Pure',		'Miner MK3',	'480',	'1',	{}) #Max Output Capped by Belt MK5
#Recipe('Raw Quartz',	'Impure',	'Miner MK3',	'120',	'1',	{}) #None In Game
Recipe('Raw Quartz',	'Normal',	'Miner MK3',	'240',	'1',	{})
Recipe('Raw Quartz',	'Pure',		'Miner MK3',	'480',	'1',	{}) #Max Output Capped by Belt MK5
Recipe('S.A.M. Ore',	'Impure',	'Miner MK3',	'120',	'1',	{})
Recipe('S.A.M. Ore',	'Normal',	'Miner MK3',	'240',	'1',	{})
#Recipe('S.A.M. Ore',	'Pure',		'Miner MK3',	'480',	'1',	{}) #Max Output Capped by Belt MK5, None In Game
Recipe('Sulfur',		'Impure',	'Miner MK3',	'120',	'1',	{})
Recipe('Sulfur',		'Normal',	'Miner MK3',	'240',	'1',	{})
Recipe('Sulfur',		'Pure',		'Miner MK3',	'480',	'1',	{}) #Max Output Capped by Belt MK5, None In Game
#Recipe('Uranium',		'Impure',	'Miner MK3',	'120',	'1',	{}) #None In Game
Recipe('Uranium',		'Normal',	'Miner MK3',	'240',	'1',	{})
#Recipe('Uranium',		'Pure',		'Miner MK3',	'480',	'1',	{}) #Max Output Capped by Belt MK5, None In Game

print(allRecipes)