# Asking for Input Sentence
text = str(input("Enter the Text:   "))
text = text.lower()
# Defining Dictionary
freq = {}

for i in text:
	if i in freq:
		freq[i] += 1
	else:
		freq[i] = 1

print ("Count of all characters in the Sentence is :\n "
										+ str(freq))
