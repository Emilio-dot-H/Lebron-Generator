from PyDictionary import PyDictionary


prime_syn = []
other_syn = []
LeTotal = []

def get_synonyms(word):
	dictionary = PyDictionary()
	synonyms = dictionary.synonym(word)
	print(synonyms)
	return synonyms


def LeTransform(title, LeList):
	title.lower()
	#turn words into list elements
	title = [_ for _ in title]
	length = len(title)

	#logic: for lebron generator
	if length<2:
		return

	elif title[1] == 'e' and (length >= 6):
		title[0] = 'L'
		title[2] = title[2].upper()
		title = "".join(title)
		prime_syn.append(title)
		LeList.append(title)

	elif title[0] == 'b' and (length >= 6):
		title = ['L', 'e'] + title
		title[2] = title[2].upper()
		title = "".join(title)
		prime_syn.append(title)
		LeList.append(title)

	elif title[0] == 'e' and (length >= 6):
		title = ['L'] + title
		title[2] = title[2].upper()
		title = "".join(title)
		prime_syn.append(title)
		LeList.append(title)

	else:
		title = ['L', 'e'] + title
		title[2] = title[2].upper()
		title = "".join(title)
		other_syn.append(title)
		LeList.append(title)

	return LeList

def LeGenerator(syn, blanklist):
	if syn is None:
		invalid_word(syn)
		return

	for x in syn:
		LeTransform(x, blanklist)
	return blanklist

def invalid_word(syn):
	error_msg = "Unfortunately, the word you've entered is not in our word bank. Please try a different word."
	syn = []
	return error_msg, syn

def get_primesyn():
	return prime_syn

def get_othersyn():
	return other_syn

# #CMND LINE INPUT
# entry = input("Enter word to LeTransform: ")

# #DEBUG
# # #Retrieve list of synonyms for entry
# synonyms = get_synonyms(entry)

# # DEBUG
# # #first word
# LeTransform(entry, LeTotal)
# LeGenerator(synonyms, LeTotal)

# amount_of_prime = len(prime_syn)
# amount_of_other = len(other_syn)
# total_of = amount_of_prime + amount_of_other

# #COMMAND LINE PRINT - DEBUG
# print("\nWord: ", LeTotal[0], "\n")
# print("\n".join([" || ".join(prime_syn[i:i+3]) for i in range(0,len(prime_syn),3)]))
# print("\n---\n")
# print("\n".join([" || ".join(other_syn[i:i+3]) for i in range(0,len(other_syn),3)]))
