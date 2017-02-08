#function to count the number of occurences a word makes in a sentence
def word_count(word):
	word_count = word.split() 
	word_count = {}
	for word in word_count: 
		word_count[word] +1
	else:
		word_count[word] = 1
	for key, value in sorted(word_count.items(), key = operator.itemgeter(1)):
		print ('key,value')