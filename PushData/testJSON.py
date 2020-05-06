import json

texte1="""


	["intellect"] = 21,
	["negBuffArmor"] = 507,
	["blockChance"] = 4.84000015258789,
	["currently_equipped"] = {
		-1, -- [1]
		-1, -- [2]
		-1, -- [3]
		2575, -- [4]
		2648, -- [5]
		2690, -- [6]
		6084, -- [7]
		1731, -- [8]
		2396, -- [9]
		2397, -- [10]
		-1, -- [11]
		-1, -- [12]
		-1, -- [13]
		-1, -- [14]
		1497, -- [15]
		1198, -- [16]
		-1, -- [17]
		-1, -- [18]
		-1, -- [19]
	},
	["currently_equipped_icon"] = {
		-1, -- [1]
		-1, -- [2]
		-1, -- [3]
		135029, -- [4]
		132624, -- [5]
		132495, -- [6]
		134583, -- [7]
		132535, -- [8]
		132602, -- [9]
		132938, -- [10]
		-1, -- [11]
		-1, -- [12]
		-1, -- [13]
		-1, -- [14]
		133754, -- [15]
		135350, -- [16]
		-1, -- [17]
		-1, -- [18]
		-1, -- [19]
	},
	["agility"] = 29,
	["level"] = 13,
	["spirit"] = 24,
	["raceID"] = "Humain",
	["bags_icon"] = {
		"backpack", -- [1]
		{
			133968, -- [1]
			132815, -- [2]
			133975, -- [3]
			133948, -- [4]
			134534, -- [5]
			134743, -- [6]
			133964, -- [7]
			133972, -- [8]
			133581, -- [9]
			132794, -- [10]
			133752, -- [11]
		}, -- [2]
		133634, -- [3]
		{
			134414, -- [1]
			134185, -- [2]
			133628, -- [3]
			134341, -- [4]
			135997, -- [5]
		}, -- [4]
		133637, -- [5]
		{
			135420, -- [1]
			132794, -- [2]
		}, -- [6]
		133639, -- [7]
		{
		}, -- [8]
		{
		}, -- [9]
	}',
	["bags"] = {
		"backpack", -- [1]
		{
			4541, -- [1]
			1179, -- [2]
			4536, -- [3]
			2070, -- [4]
			4604, -- [5]
			1177, -- [6]
			4540, -- [7]
			729, -- [8]
			1191, -- [9]
			159, -- [10]
			1434, -- [11]
		}, -- [2]
		4496, -- [3]
		{
			6948, -- [1]
			732, -- [2]
			2806, -- [3]
			723, -- [4]
			731, -- [5]
		}, -- [4]
		5572, -- [5]
		{
			4562, -- [1]
			814, -- [2]
		}, -- [6]
		1537, -- [7]
		{
		}, -- [8]
		{
		}, -- [9]
	},
	["maxpower"] = 100,
	["haste"] = 3.20000004768372,
	["percentmod"] = 45.6285743713379,
	["gender"] = 2,
	["classID"] = "Guerrier",
	["basePower"] = 99,
	["parryChance"] = 4.84000015258789,
	["dodgeChance"] = 4.67429971694946,
	["name"] = "Banzai",
	["critChance"] = 4.83430004119873,
	["stamina"] = 35,
	["strength"] = 40,
	["maxHealth"] = 288,
	["localizedFaction"] = "Alliance",




"""

def stringIntoJSON(savedVariablesString):
    savedVariablesString = savedVariablesString.replace('["', '"')
    savedVariablesString = savedVariablesString.replace('"]', '"')
    savedVariablesString = savedVariablesString.replace('=', ': ')
    #savedVariablesString = savedVariablesString.replace('"', " ' ")
    savedVariablesString = savedVariablesString.replace(" ", "")
    savedVariablesString = savedVariablesString.replace("\n", "")
    savedVariablesString = savedVariablesString.replace("true", "True")
    savedVariablesString = savedVariablesString.replace("false", "False")
    savedVariablesString = savedVariablesString.replace(":{", ":[")
    savedVariablesString = savedVariablesString.replace("{", "[")
    savedVariablesString = savedVariablesString.replace("}","]")
    for i in range(0,20):
        savedVariablesString =savedVariablesString.replace("--["+str(i)+"]","")
    savedVariablesString = savedVariablesString.replace(",	]","]")
    savedVariablesString = savedVariablesString.replace(",		]","]")
    savedVariablesString = savedVariablesString.replace("]'","]")
    stringResult="{"+ savedVariablesString+ "}"
    stringResult=stringResult.replace(",}","}")
    return stringResult

texte2="""{"localizedFaction" : "Alliance","bags" : ["backpack" , [1,2,3]]}"""
# dict=json.loads(texte2) #convertit une chaine de caractère au format JSON en un dictionnaire
# print((dict['bags'][0]))
jsonString=stringIntoJSON(texte1)
print(jsonString)
# dict=json.loads(jsonString)


stringDebug="""{	"intellect":21,	"negBuffArmor":507,	"blockChance":4.84000015258789,	"currently_equipped":[		-1,		-1,		-1,		2575,		2648,		2690,		6084,		1731,		2396,		2397,		-1,		-1,		-1,		-1,		1497,		1198,		-1,		-1,		-1],	"currently_equipped_icon":[		-1,		-1,		-1,		135029,		132624,		132495,		134583,		132535,		132602,		132938,		-1,		-1,		-1,		-1,		133754,		135350,		-1,		-1,		-1],	"agility":29,	"level":13,	"spirit":24,	"raceID":"Humain",	"bags_icon":[		"backpack",		[			133968,			132815,			133975,			133948,			134534,			134743,			133964,			133972,			133581,			132794,			133752],		133634,		[			134414,			134185,			133628,			134341,			135997],		133637,		[			135420,			132794],		133639,		[		],		[		]]} """
dictDebug=json.loads(jsonString)
print(dictDebug["bags_icon"])