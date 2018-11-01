import re
import numpy as np
import matplotlib.pyplot as plt


#Finds words over 15 letters long, and plots them in a histogram.
def long_word(words):
	#opens text file
	file = open(words, 'r', encoding="utf8")
	#creates a list of words for each line in the text
	txt_split = [line.rstrip('\n') for line in file]

	#joins text into one item
	txt_joined = " ".join(txt_split)
	#splits each word of the document to an item in a list
	txt_list = txt_joined.split(" ")
	# create empty dictionary for word:frequency pairs
	freq = {}

	#finds words over 15 characters and places them in the dictionary
	for item in txt_list:

		#removes punctuation
		item = re.sub('\.|\!|\?|\,|\(|\)|\;|\:', '', item)
		#removes left and right quotations
		item = re.sub(u'[\u201c\u201d]', '', item)


		if len(item) >= 15:
			#skips over dashed and em-dashed words
			if "-" in item:
				continue
			elif "—" in item:
				continue
			elif item in freq:
				freq[item] += 1
			else:
				freq[item] = 1
	print(freq)

	#Turns dictionary to tuples so they can be sorted
	words, count = zip(*freq.items())
	#provides the index sort to apply to both arrays, decending by count, cutting list off at 10 items
	indexSort = np.argsort(count)[::-1]
	words = np.array(words)[indexSort]
	words = words[0:10]
	count = np.array(count)[indexSort]
	count = count[0:10]
	indicies = np.arange(len(words[:10]))

	plt.bar(indicies, count)

	plt.xticks(indicies, words)

	plt.show()
	#final = freq.most_common
	return freq


if __name__ == "__main__":
	long_word("wap_notoc.txt")
