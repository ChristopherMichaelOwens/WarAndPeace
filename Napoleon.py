import re
import numpy as np
import matplotlib.pyplot as plt

#Identifies the number of times Napoleon is mentioned on a per book basis
def napoleon_freq(words):
	# opens text file
	file = open(words, 'r', encoding="utf8")
	# creates a list of words for each line in the text
	txt_split = [line.rstrip('\n') for line in file]

	# joins text into one item
	txt_joined = " ".join(txt_split)
	# splits each word of the document to an item in a list
	txt_list = txt_joined.split(" ")
	mentioned = {}
	book = 0
#iterates through the document, with the index starting at 1, through all but the last, and adding 3 word phrases to a list
	for i in range(len(txt_list)):
		#removes extra characters, dash or em dash is acceptable
		txt_list[i] = re.sub('\.|\!|\?|\,|\(|\)|\;|\:|\*', '', txt_list[i])
		# removes left and right quotations
		txt_list[i] = re.sub(u'[\u201c\u201d]', '', txt_list[i])
		#creates dictionary (key:number) to (value:list of words).
		# Finds mention of Napoleon, Bonaparte, Napoleon Bonaparte, or Buonaparte and adds it to the bin number.
		if "BOOK" in txt_list[i]:
			book += 1
		if "Napoleon" in txt_list[i] and "Bonaparte" in txt_list[i+1]:
			if book in mentioned:
				mentioned[book] += 1
			else:
				mentioned[book] = 1
		elif "Napoleon" in txt_list[i]:
			if book in mentioned:
				mentioned[book] += 1
			else:
				mentioned[book] = 1
		elif "Bonaparte" in txt_list[i] and "Napoleon" not in txt_list[i-1]:
			if book in mentioned:
				mentioned[book] += 1
			else:
				mentioned[book] = 1
		if "Buonaparte" in txt_list[i]:
			if book in mentioned:
				mentioned[book] += 1
			else:
				mentioned[book] = 1

	for key in mentioned:
		print("Book " + str(key) + ": " + str(mentioned[key]) )




if __name__ == "__main__":
	napoleon_freq("wap_notoc.txt")
