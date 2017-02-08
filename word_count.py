#function to count the number of occurences a word makes in a sentence
def word_count(word):

	#split the words in the sentence then create a blank dict to store words.
	word_count = word.split() 
	word_count = {} 

	#loops through the words in the sentence.
	# for each word looped through existing in the dict, increment
	#if not already in dict, add it to dict and assign 1
	for word in word_count: 
		word_count[word] +1
	else:
		word_count[word] = 1
	#sort dict based on the frequency of occurence of a word. sort by value	
	for key, value in sorted(word_count.items(), key = operator.itemgeter(1)):
		print ('key,:value')