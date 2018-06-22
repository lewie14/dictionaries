#Scrabble Exercise
print("========================Scrabble Exercise=================")

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#Using a list comprehension and zip, create a dictionary called letter_to_points that 
#has the elements of letters as the keys and the elements of points as the values.

zipped_letters = zip(letters, points)
letter_to_points = {key: value for key, value in zipped_letters}
print(zipped_letters)
print(letter_to_points )

print()

letter_to_points[""] = 0

#We want to create a function that will take in a word and return how many points that word is worth.
# If the letter you are checking for is not in letter_to_points, add 0 to the point_total.
def score_words(word):
  point_total = 0
  for letters in word:
    point_total += letter_to_points.get(letters, 0)
  return point_total

brownie_points = score_words("BROWNIE")
#Should give 15
print(brownie_points)

players_to_words = {"player1":["BLUE", "TENNIS", "EXIT"], "wordNerd":["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_points = {}
#terate through the items in player_to_words. Call each player player and each list of words words.
for player, words in players_to_words.items():
	player_points = 0
	#Within the loop, create another loop that goes through each word in words and adds the value of score_word() with word as an input.
	for word in words:
		player_points += score_words(word)
#After the inner loop ends, set the current player value to be a key of player_to_points, with a value of player_points.
	player_to_points[player] = player_points 
	
print(player_to_points)

'''

If you want extended practice, try to implement some of these ideas with the Python you've learned:

play_word() — a function that would take in a player and a word, and add that word to the list of words they've played
update_point_totals() — turn your nested loops into a function that you can call any time a word is played
make your letter_to_points dictionary able to handle lowercase inputs as well
'''
