user_input = str(input("Enter a Phrase: "))
wordList = user_input.split()
acronyms = " "
for i in wordList:
    acronyms = acronyms+str(i[0]).upper()
print(acronyms)
