print("--------------------Get a Key------------------------")

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
print(zodiac_elements["earth"])
print(zodiac_elements["fire"])

print()
print("--------------------Get an invalid Key------------------------")

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
zodiac_elements["energy"] = "Not a Zodiac element"
print(zodiac_elements["energy"])

print()
print("--------------------Try/Except to Get a Key-----------------------")

caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}

try:
  print(caffeine_level["matcha"])
except KeyError:
 print("Unknown Caffeine Level") 

caffeine_level["matcha"] = 30

try:
  print(caffeine_level["matcha"])
except KeyError:
 print("Unknown Caffeine Level") 


print()
print("--------------------Try/Except to Get a Key-Safely ---------")

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

#teracoder is in the dictionary so output is 10019
tc_id = user_ids.get("teraCoder", 100000)
print(tc_id)
#superStackSmash is not in dictionary so output is 100000
stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id)

print()
print("--------------------Delete a Key---------")

raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}

#watch as raffle tickets are won how they are removed from the dictionary
print(raffle)
print(raffle.pop(320291, "No Prize"))
#gives "Gift Basket"
print(raffle)
#gives {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
print(raffle.pop(100000, "No Prize"))
#gives "No Prize"
print(raffle)
#gives {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
print(raffle.pop(872921, "No Prize"))
#gives "Concert Tickets"
print(raffle)


available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20
print(available_items)
print("Health Points are " + str(health_points))

# In one line, add the value of "stamina grains" to health_points and remove the item from the dictionary. 
#If the key does not exist, add 0 to health_points
health_points += available_items.pop("stamina grains", 0)
print(available_items)
print("Health Points are " + str(health_points))

#In one line, add the value of "power stew" to health_points and remove the item from the dictionary. 
#If the key does not exist, add 0 to health_points.
health_points += available_items.pop("power stew", 0)
print(available_items)
print("Health Points are " + str(health_points))

#In one line, add the value of "mystic bread" to health_points and remove the item from the dictionary. 
#If the key does not exist, add 0 to health_points
health_points += available_items.pop("mystic bread", 0)
print(available_items)
print("Health Points are " + str(health_points))

print()
print("--------------------Get all Keys--------")

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()
lessons = num_exercises.keys()

print(users)
print(lessons)

test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
for student in test_scores.keys():
  print(student)
  
print()
print("--------------------Get all Values--------")

test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}

for score_list in test_scores.values():
  print(score_list)
  
#list(test_scores.values())
print()
print()
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0
print(num_exercises)
for exercises in num_exercises.values():
  total_exercises += exercises
  print(total_exercises)
print(total_exercises)

print()
print("--------------------Get all Items-------")

biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}

for company, value in biggest_brands.items():
  print(company + " has a value of " + str(value) + " billion dollars. ")
print()
print()

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for position, value in pct_women_in_occupation.items():
  print("Women make up " + str(value) + " percent of " + position + "s")

print()
print()
tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread ={}

spread["past"] = tarot.pop(13)

spread["present"] = tarot.pop(22)

spread["future"] = tarot.pop(10)

for key, value in spread.items():
  print("Your " + key + " is the " + value + " card.")

print()
print()
oscars = {"Best Picture": "Moonlight", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

for element in oscars.values():
  print(element)


print()
print()
combo_meals = {1: ["hamburger", "fries"], 2: ["hamburger", "fries", "soda"], 4: ["veggie burger", "salad", "soda"], 6: ["hot dog", "apple slices", "orange juice"]}
#print(combo_meals[3])
print(combo_meals[2])

print()
print()
inventory = {"iron spear": 12, "invisible knife": 30, "needle of ambition": 10, "stone glove": 20, "the peacemaker": 65, "demonslayer": 50}
print(inventory.get("stone glove", 30))

print()
print()
inventory = {"iron spear": 12, "invisible knife": 30, "needle of ambition": 10, "stone glove": 20, "the peacemaker": 65, "demonslayer": 50}

print(12 in inventory)

print()
print()

oscars = {"Best Picture": "Moonlight", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

for element in oscars:
  print(element)

print()
print()
combo_meals = {1: ["hamburger", "fries"], 2: ["hamburger", "fries", "soda"], 4: ["veggie burger", "salad", "soda"], 6: ["hot dog", "apple slices", "orange juice"]}
print(combo_meals.get(3, ["hamburger", "fries"])

print()
print()
raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}

raffle.pop(561721, "No Value")
print(raffle)
