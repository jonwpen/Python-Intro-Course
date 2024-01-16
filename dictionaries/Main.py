# Dictionaries are sets of key value pairs. They are like HashMaps in Java.
# Syntax:
menu = {"avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
# Values can be any type: string, integer, list, or even dictionary:
person = {"name": "Shuri", "age": 18, "family": ["T'Chaka", "Ramonda"]}
# A key cannot be a list or a dictionary. These are not hashable.
# You can create an empty dictionary

# Adding a pair to a dictionary:
animals_in_zoo = {}
animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurs"] = 0
print(animals_in_zoo)

# Adding multiple keys at once:
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)

# Overwriting values:
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners["Supporting Actress"] = "Viola Davis"
oscar_winners["Best Picture"] = "Moonlight"

# Dict Comprehension:
# To combine two lists into a dictionary:
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {k: v for k, v in zipped_drinks}
# or just with one line:
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]
students = {key: value for key, value in zip(names, heights)}
# students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}

# zip() combines 2 lists into an iterator of tuples
# dict comprehension takes a pair from the iterator
# names the elements in the pair key and value
# creates a key: value item in the students dictionary
# repeats for the entire iterator of pairs

# USING DICTIONARIES
# To access a value, provide the key:
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
print(zodiac_elements["earth"])
print(zodiac_elements["fire"])

# To avoid an error when checking for an invalid key, use an if statement:
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599,
                    "Lotte World Tower": 554.5, "One World Trade": 541.3}
key_to_check = "Landmark 81"
if key_to_check in building_heights:
    print(building_heights["Landmark 81"])

# Safely get a key:
# You can also use the .get() method to check for a key. It will return 'none' if it does not exist.
# In the .get(), you can set a default value to return if it does not exist:
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599,
                    "Lotte World Tower": 554.5, "One World Trade": 541.3}
#this line will return 632:
building_heights.get("Shanghai Tower")
#this line will return None:
building_heights.get("My House")
print(building_heights.get('Shanghai Tower', 0))  # Prints 632
print(building_heights.get('Mt Olympus', 0))  # Prints 0
print(building_heights.get('Kilimanjaro', 'No Value'))  # Prints 'No Value'

# Delete a key using .pop() method. Just like with .get(), you can define a default value to return if the key does not
# exist:
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20
health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)
# ^ This pops the key value pair and returns the value or returns 0 if the key does not exist.
print(available_items)
print(health_points)

# To operate on all keys in a dictionary, you can use the list() function.
# To view all keys but not operate on them, you can use
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
print(list(test_scores))
# Prints ["Grace", "Jeffrey", "Sylvia", "Pedro", "Martin", "Dina"]
for student in test_scores.keys():
    print(student)

# To get all values, use .values().
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
for score_list in test_scores.values():
    print(score_list)
# You can also use this, but it mostly isn't necessary because the dict_values object returned by .values() will work
# just fine for most operations:
list(test_scores.values())

# To get all key AND values, use .item(). It returns a tuple containing the key and value.
biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}
for company, value in biggest_brands.items():
    print(company + " has a value of " + str(value) + " billion dollars. ")

# last example:
tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread = {}

spread["past"] = tarot.pop(13)
spread["present"] = tarot.pop(22)
spread["future"] = tarot.pop(10)

for k, v in spread.items():
    print("Your " + k + " is the " + v + " card.")

# Final project: Scrabble
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {k: v for k, v in zip(letters, points)}

letter_to_points[" "] = 0

def score_word(word):
    point_total = 0
    for letter in word:
        if letter not in word:
            point_total += 0
        else:
            point_total += letter_to_points[letter]
    return point_total

brownie_points = score_word("BROWNIE")
print(brownie_points)

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"],
    "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_points = {}
for player, words in player_to_words.items():  # You need .items() to iterate through both k and v
    player_points = 0
    for word in words:
        player_points += score_word(word)
    player_to_points[player] = player_points

print(player_to_points)
