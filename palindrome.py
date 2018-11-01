import re
import numpy as np
import matplotlib.pyplot as plt

#Identifies the longest palindrome in the text, excluding lists of spaces
def palindrome(words):
	# opens text file
	file = open(words, 'r', encoding="utf8")
	# creates a list of words for each line in the text
	txt_split = [line.rstrip('\n') for line in file]

	# joins text into one item
	txt_joined = " ".join(txt_split).lower()
	#set variables for longest palindrome length, and its text
	longest_pal_length = 0
	longest_pal_text = ""
#iterates through the document, with the index starting at 1, through all but the last, and adding 3 word phrases to a list
	for i in range(len(txt_joined)):
		#case 1: single value in middle
		if i + longest_pal_length > len(txt_joined):
			break
		if txt_joined[i] + txt_joined[i+1] == "  ":
			continue
		#case 1: single value in middle
		if txt_joined[i-1] == txt_joined[i+1]:
			length = 2
			#checking for palindrome, with safety of 800 characters
			while True:
				if length > 800:
					break
				elif "  " in txt_joined[i - length: i + 1 + length]:
					break
				elif txt_joined[i + length] == txt_joined[i - length]:
					if 2*length+1 > longest_pal_length:
						longest_pal_length = 2*length + 1
						longest_pal_text = txt_joined[i - length: i + 1 + length]
					length += 1
				else:
					break
		#case2 double value in middle
		elif txt_joined[i] == txt_joined[i+1]:
			length = 1
			#checking for palindrome with safety of 800 characters
			while True:
				if length > 800:
					break
				elif "  " in txt_joined[i-length :i + 2 + length]:
					break
				elif txt_joined[i + 1 + length] == txt_joined[i - length]:
					if 2*length + 2 > longest_pal_length:
						longest_pal_length = 2*length + 2
						longest_pal_text = txt_joined[i-length :i + 2 + length]
					length += 1
				else:
					break
		print(longest_pal_text)
		print(longest_pal_length)
	print(longest_pal_text)
	print(longest_pal_length)





if __name__ == "__main__":
	palindrome("wap_notoc.txt")
