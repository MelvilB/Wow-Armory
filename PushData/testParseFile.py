import requests
import ast
import json
text="""

savedplayer = {
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



}

 """
testText="""savedplayer ={["localizedFaction"] = "Alliance",
                        ["bags"] = [1,2,3],                    
}

"""
def luaFileToPython(savedVariablesString):
    newString=" "
    # for i in range(len(savedVariablesString)):
    #     if savedVariablesString[i]=='[' or savedVariablesString[i]==']':
    #         newString=newString+' '
    #     if savedVariablesString[i]=='=':
    #         newString=newString+':'
    #     else:
    #         newString=newString+savedVariablesString[i]
    savedVariablesString=savedVariablesString.replace('["','"')
    savedVariablesString=savedVariablesString.replace('"]','"')
    savedVariablesString=savedVariablesString.replace('=',': ')
    #savedVariablesString=savedVariablesString.replace('"'," ' ")
    savedVariablesString=savedVariablesString.replace(" ","")
    savedVariablesString=savedVariablesString.replace("\n","")
    savedVariablesString=savedVariablesString.replace("true","True")
    savedVariablesString=savedVariablesString.replace("false","False")
    savedVariablesString = savedVariablesString.replace(":{", ":[")
    savedVariablesString = savedVariablesString.replace("{", "[")
    savedVariablesString = savedVariablesString.replace("}", "]")
    for i in range(0, 20):
        savedVariablesString = savedVariablesString.replace("--[" + str(i) + "]", "")
    savedVariablesString = savedVariablesString.replace(",	]", "]")
    savedVariablesString = savedVariablesString.replace(",		]", "]")
    savedVariablesString = savedVariablesString.replace("]'", "]")
    stringResult = "{" + savedVariablesString + "}"
    stringResult = stringResult.replace(",}", "}")
    return stringResult

def getSettings(name):
    index=text.find(name)
    text2=text[index:]
    #print(text2[text2.find('{')+1:text2.find('}')])
    return(text2[text2.find('{')+1:len(text2)-4]) # permet d'enlever les accolades de début et fin


def getSettingsValue(name):
    index=text.find(name)
    text2=text[index:]
    return(text2[text2.find('=')+1:text2.find(',')])
stringInit=getSettings("savedplayer")
# stringInit = stringInit.replace("{","")
# stringInit = stringInit.replace("}","")
print(stringInit)

jsonString=luaFileToPython(stringInit)
print(jsonString)
dictDebug=json.loads(jsonString)
print(dictDebug["bags_icon"])








