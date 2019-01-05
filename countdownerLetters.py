
#Take 9 random letters as inputLetters
x = input('Please enter 9 letters (at least 2 vowels!): ')

while len(x) != 9 or not x.isalpha():
	x = input('Please enter only 9 letters (at least 2 vowels!): ')

vowels = ['a', 'e', 'i', 'o', 'u']


inputLetters = list(x)




#Make list of the other 17 letters as notInputLetters
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

notInputLetters = []

for w in alphabet:
	if w not in inputLetters:
		notInputLetters.append(w)


#Import OLD wordlist

with open('C:/Users/pierr/Documents/Web Design/NLPpythong/words_alpha.txt', 'r') as f:
	wordList = f.read().splitlines()

#Make list with max 9 letter words

maxNineLetterWordList = [w for w in wordList if len(w) < 10]


#Make subList from words starting with each of the inputLetters
subList = []
for letter in inputLetters:
	x = [w for w in maxNineLetterWordList if w.startswith(letter)]
	subList = subList + x


# check if 
haveLettersList = []
for word in subList:
	should_include = True
	for excluded_letter in notInputLetters:
		if excluded_letter in word:
			should_include = False
	if should_include:
		haveLettersList.append(word) 		



#Make letterScore for each letter in inputLetters

inputLetterScore = dict((x, inputLetters.count(x)) for x in set(inputLetters))

finalList = []
for word in haveLettersList:
	wordListed = list(word)
	wordScore = dict((y, wordListed.count(y)) for y in set(wordListed))
	# parsedInputLetterScore = []
	if all(inputLetterScore[k] == wordScore[k] for k in wordScore):
		finalList.append(word)

finalList = set(finalList)

print("Here are all the 9 letter words: ")
print([w for w in finalList if len(w) == 9])

print("Here are all the 8 letter words: ")
print([w for w in finalList if len(w) == 8])

print("Here are all the 7 letter words: ")
print([w for w in finalList if len(w) == 7])

print("Here are all the 6 letter words: ")
print([w for w in finalList if len(w) == 6])

print("Here are all the 5 letter words: ")
print([w for w in finalList if len(w) == 5])

print("Here are all the 4 letter words: ")
print([w for w in finalList if len(w) == 4])

print("Here are all the 3 letter words: ")
print([w for w in finalList if len(w) == 3])

print("Here are all the 2 letter words: ")
print([w for w in finalList if len(w) == 2])

print("Here are all the 1 letter words: ")
print([w for w in finalList if len(w) == 1])





