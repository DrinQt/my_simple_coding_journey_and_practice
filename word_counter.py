#print the purpose of the program
print("This program counts the number of words in a sentence.")

#prompt the user to enter a sentence
sentence = input("Enter a sentence: ")

#count the number of words in the sentence
word_count = len(sentence.split())

#display the number of words in the sentence
print("The sentence has", word_count, "words.")