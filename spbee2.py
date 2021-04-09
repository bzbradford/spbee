import string

dictionary = open("dict/dictionary.txt", "r", errors = "ignore")
wordlist = dictionary.read().splitlines()
wordlist = [word.upper() for word in wordlist]

keyletter = "T"
optletters = sorted(list("UAHYRW"))
inletters = list(keyletter) + optletters
outletters = sorted(list(set(string.ascii_uppercase).difference(inletters)))

print("Key letter: " + "A")
print("Optional letters: " + ", ".join(optletters))
print("Forbidden letters: " + ", ".join(outletters))
print("")

# find words with key letter
wordlist = [word for word in wordlist if keyletter in word]

# remove words without the letters
for l in outletters:
    wordlist = [word for word in wordlist if l not in word]

# keep only long enough words
wordlist = [word for word in wordlist if len(word) >= 4]
#wordlist = sorted(wordlist, key = lambda w: len(w), reverse = True)

# how many words
print(str(len(wordlist)) + " words found!\n")

with open('out.txt', 'w') as file:
	for word in wordlist:
		print(word)
		file.write('%s\n' % word)