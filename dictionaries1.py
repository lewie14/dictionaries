print("--------Add to an empty dictionary----------------------------")
# Add to an empty dictionary

animals_in_zoo ={}

animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurs"] = 0

print(animals_in_zoo)

print("-----------Add multiple keys_-------------------------------")
#-------------Add multiple keys------------------------

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238} 

user_ids.update({"theLooper": 138475 , "stringQueen": 85739})

print(user_ids)

print("-----------Overwrite values-------------------------------")
#-------------Overwrite values ----------------------

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

oscar_winners["Supporting Actress"] = "Viola Davis"
print(oscar_winners)
oscar_winners["Best Picture"] = "Moonlight"
print(oscar_winners)

print("------List Comprehensions to Dictionaries---------------")
#--------List Comprehensions to Dictionaries-----------

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {key: value for key, value in zipped_drinks}
print(zipped_drinks)
print(drinks_to_caffeine)

print("------Review--------------")
#--------Review-----------------------------

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
#create a dictionary songs:playcount
plays = {song:playcount for [song, playcount] in zip(songs, playcounts)}

#Add the following. Respect is an overwrite, the other an addition
plays["Respect"] = 94
plays["Purple Haze"] = 1

# create a new dictionary for best songs and sunday feelings made from plays and an empty dictionary
library = {"The Best Songs": plays, "Sunday Feelings": {}}

print(library)

inventory = {"iron spear": 12, "invisible knife": 30, "needle of ambition": 10, "stone glove": 20, "the peacemaker": 65, "demonslayer": 50}

print("the peacemaker" in inventory)


