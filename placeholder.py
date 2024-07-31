# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

def moneyConversion(damages):
  damagesConverted = []

  for x in damages:
    if x == "Damages not recorded":
      damagesConverted.append(x)
    elif 'M' in x:
      x = float(x.strip('M'))
      damagesConverted.append(x * 1000000)
    elif 'B' in x:
      x = float(x.strip('B'))
      damagesConverted.append(x * 1000000000)

  return damagesConverted


# test function by updating damages

damagesConverted = moneyConversion(damages)
print(damagesConverted)

# 2 
# Create a Table
myDict = {}
# Create and view the hurricanes dictionary
for index in range(0, 34):
  myDict.update({names[index]:{"Name": names[index],
    "Month": months[index],
    "Year": years[index],
    "Max Sustained Wind": max_sustained_winds[index],
    "Areas Affected": areas_affected[index],
    "Damage": damagesConverted[index],
    "Deaths": deaths[index]
  }})

#print(myDict)
# 3
# Organizing by Year
def organizeByYear(dict):
	newDict = {}
   
	for index in range(0,34):
		year = dict[names[index]]["Year"]
        
		if year in newDict:
			newList = [newDict[year]]
			newList.append({"Name": names[index],
				"Month": months[index],
				"Year": years[index],
				"Max Sustained Wind": max_sustained_winds[index],
				"Areas Affected": areas_affected[index],
				"Damage": damagesConverted[index],
				"Deaths": deaths[index]
			})
            
			newDict.update({year:newList})

		else:
			newDict.update({year:{"Name": names[index],
			"Month": months[index],
			"Year": years[index],
			"Max Sustained Wind": max_sustained_winds[index],
			"Areas Affected": areas_affected[index],
			"Damage": damagesConverted[index],
			"Deaths": deaths[index]
			}})

	return newDict
    
# create a new dictionary of hurricanes with year and key
newDict = organizeByYear(myDict)
print(newDict)

# 4
# Counting Damaged Areas
def countImpact(list):
    NumOfAffect = { }
    
    for x in list:
        for y in x:
            if y not in NumOfAffect.keys():
                NumOfAffect.update({y:1})
            else:
                NumOfAffect.update({y:NumOfAffect[y] + 1})
                
    return NumOfAffect

numOfAffect = countImpact(areas_affected)
print(numOfAffect)   

# create dictionary of areas to store the number of hurricanes involved in


# 5 
# Calculating Maximum Hurricane Count
def mostAffected(dict):
  mostAffectedArea = {}
  max_area_count = 0
  max_area = ""
    
  for x in dict.keys():
    if dict[x] > mostAffected:
      max_area_count = dict[x]
      max_area = x

  mostAffectedArea.update({max_area:max_area_count})
  return mostAffectedArea

# find most frequently affected area and the number of hurricanes involved in
mostAffectedArea = mostAffected(numOfAffect)
print(mostAffectedArea)
	

# find most frequently affected area and the number of hurricanes involved in


# 6
# Calculating the Deadliest Hurricane
def deadliestHurricanes(dict):
    deadliest = {}
    maxNumOfDeaths = 0
    deadlyHurricane= ""
    
    for x in dict.keys():
        if (dict[x]["Deaths"] > maxNumOfDeaths):
            deadlyHurricane = x
            maxNumOfDeaths = dict[x]["Deaths"]

    deadliest.update({deadliestHurricanes:maxNumOfDeaths})
    return deadliest
        
# find highest mortality hurricane and the number of deaths
deadliestHurricane = deadliestHurricanes(myDict)
print(deadliestHurricane)
# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

def mortalityRating(dict):
    rating = {0:[],
              1:[],
              2:[],
              3:[],
              4:[],
              5:[]}
    
    for x in dict.keys():
        for y in mortality_scale.keys():
            if (dict[x]["Deaths"] > mortality_scale[y]):
                rating[y].append(dict[x]["Name"])
                
    return rating
                

# categorize hurricanes in new dictionary with mortality severity as key
rating = mortalityRating(myDict)
print(rating)

# 8 Calculating Hurricane Maximum Damage
def maxDamage(dict):
    maxHurricane = {}
    costHurricane = 0
    costHurricanName = ""

    for x in dict.keys():
        if (dict[x]["Damage"] > costHurricane):
            costHurricane = dict[x]["Damage"]
            costHurricanName = dict[x]["Name"]
            
    maxHurricane.update({costHurricanName:costHurricane})
    return maxHurricane
# find highest damage inducing hurricane and its total cost
highestDamageHurricane = maxDamage(myDict)
print(highestDamageHurricane)

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

def damageRating(dict):
    rating = {0:[],
              1:[],
              2:[],
              3:[],
              4:[],
              5:[]}
    
    for x in dict.keys():
        for y in damage_scale.keys():
            if (dict[x]["Damage"] > damage_scale[y]):
                rating[y].append(dict[x]["Damage"])
                
    return rating
  
# categorize hurricanes in new dictionary with damage severity as key
damageRatings = damageRating(myDict)
print(damageRatings)