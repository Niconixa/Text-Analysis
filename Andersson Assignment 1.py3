with open("Muller1861_lecture1.txt") as h:
        muller = h.read()
        text=muller.replace("\n", "").replace("\\", " ")
        characterlessmuller=re.sub("[.,?!'\";:]", "", text).replace("--", " ")
        #makes list of words from text
        tokenmuller = characterlessmuller.lower().split()

#Task 1
countsentences=0
for i in text:
	if i == '.':
		#i is here recognised as a full stop and the program 'counts' them in the countsentences counter
		countsentences=countsentences+1

#Task 2 (function reused for task 3)
def howmanywords(text):
	#The function splits the text variable according to empty spaces and counts the words between
	countwords = len(text.split())
	return countwords

#Task 3
def getlistofsortedsentences(text):
	#The sentence is defined as being split by full stops in the text
	sentences = text.split(".")
	#The sentences are sorted in descending order, according to the number of words, using the function howmanywords
	sortsentences=sorted(sentences, reverse=True, key=lambda sentence: howmanywords(sentence))
	#Python3 calculates an extra sentence of 1 word, which is ommitted using :-1
	return sortsentences[:-1]

def printsentences(listofsentences):
	#function to list how many words are in each sentence and to create list
	for sentence in listofsentences:
		numberofwords=len(sentence)
		#print here called in the function rather than by itself with reference to function
		print("One sentence in the text has", numberofwords, "characters")
	return
		
#Task 4
def longestwords():
	#remove punctuation from text
	characterlesstext=text.replace(".", "").replace(",", "")
	#Split text into list of words
	listofwords=characterlesstext.split()
	#sort words in descending order according to length of words
	sortwords=sorted(listofwords, reverse=True, key=lambda word: len(word))
	#create a list of the top 5 longest words
	top5=[]
	#specify want top 5 longest words from the sortwords and append them to list
	for i in range(0,5,1):
		top5.append(sortwords[i])
	top5.sort()
	return top5

print(getlistofsortedsentences(text))
print ("This text contains", countsentences, "sentences")
#print results of counter for sentences
print ("This text contains", howmanywords(text), "words")
#print result of function howmanywords
sortlist=getlistofsortedsentences(text)
#call function to sort sentences into list of number of words
printsentences(sortlist)
#print the results of the function with sorted sentences by number of words
print ("The longest words in the text are: ", ', ' .join(longestwords()))
#print top 5 longest words separated by comma, rather than as a vertical list




