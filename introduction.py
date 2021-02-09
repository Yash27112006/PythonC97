introduction = input("Introduce yourself: ")
wordCount = 1
characterCount = 0

for words in introduction:
    characterCount+=1
    print(characterCount)
    if (words==' '):
        wordCount+=1


print("Number of words in the string: ")
print(wordCount)
print("Number of characters: ")
print(characterCount)
    