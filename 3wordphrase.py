import re
import numpy as np
import matplotlib.pyplot as plt

#Identifies the 20 most common three word phrases.
def three_word(words):
	# opens text file
	file = open(words, 'r', encoding="utf8")
	# creates a list of words for each line in the text
	txt_split = [line.rstrip('\n') for line in file]

	# joins text into one item
	txt_joined = " ".join(txt_split)
	# splits each word of the document to an item in a list
	txt_list = txt_joined.split(" ")
	freq = {}
#iterates through the document, with the index starting at 1, through all but the last, and adding 3 word phrases to a list
	for index in range(1,len(txt_list)-1):
		phrase = str(txt_list[index-1]+ ' ' + txt_list[index] + ' ' + txt_list[index + 1]).lower()

		#gets rid of the phrase "*", and any junk.
		if len(phrase) < 5:
			continue
		elif phrase in freq:
			freq[phrase] += 1
		else:
			freq[phrase] = 1


	words, count = zip(*freq.items())
	#provides the index sort to apply to both arrays, decending by count
	indexSort = np.argsort(count)[::-1]
	words = np.array(words)[indexSort]
	#gets rid of space and phrases with chapter with spaces on the side, pulling 15 total phrases
	words = words[2:22]
	count = np.array(count)[indexSort]
	count = count[2:22]
	indecies = np.arange(len(words[:20]))
	words_count = zip(words,count)
	print(list(words_count))
	#Plots the histogram
	plt.bar(indecies, count)

	plt.xticks(indecies, words)

	plt.show()


if __name__ == "__main__":
	three_word("wap_notoc.txt")
