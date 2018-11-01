import re
import numpy as np
import matplotlib.pyplot as plt


#Plots the average ratio of vowels to consenants based on length of word
def ratio(words):
	# opens text file
	file = open(words, 'r', encoding="utf8")
	# creates a list of words for each line in the text
	txt_split = [line.rstrip('\n') for line in file]

	# joins text into one item
	txt_joined = " ".join(txt_split)
	# splits each word of the document to an item in a list
	txt_list = txt_joined.split(" ")
	word_length = {}
	vowels = ['a','e','i','o','u']
	for word in txt_list:
		#removes extra characters, dash or em dash is acceptable
		word = re.sub('\.|\!|\?|\,|\(|\)|\;|\:|\*', '', word)
		# removes left and right quotations
		word = re.sub(u'[\u201c\u201d]', '', word)
		#creates dictionary (key:number) to (value:list of words).
		# Measures length of each word and puts the word it in a bin in word_length.
		#gets rid of extra spaces
		if "  " in word:
			continue
		elif len(word) in word_length:
			word_length[len(word)].append(word)
		else:
			word_length[len(word)] = [word]
	print(word_length)
	density_dict = {}
	#create the vowel density
	#Goes through the words in each length bin, and counts the vowels, total count is word length
	# multiplied by the number of words in that bin.
	for key in word_length:
		if key == 0:
			continue
		vowel_count = 0
		total_count = key * len(word_length[key])
		print(total_count)
		for word in word_length[key]:
			for char in word.lower():
				if char in vowels:
					vowel_count += 1
		density_dict[key] = vowel_count / total_count

	print(density_dict)

	#creates two arrays to match the key/ratio pairs
	x = np.array([key for key in density_dict])
	y = np.array([density_dict[key] for key in density_dict])

	plt.scatter(x,y)
	plt.show()
	#what the heck is the 31 character "word"?
	print(word_length[31])

if __name__ == "__main__":
	ratio("wap_notoc.txt")
