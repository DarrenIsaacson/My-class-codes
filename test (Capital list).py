# Author == Darren Isaacson
# This program is designed to change the first letter of a sentence.

def main():
    sentences = getSentence()
    newList = sentenceSplit(sentences)
    getVerfied(newList)
    capfirstWord(newList)


def getSentence():
    sentence = input("Please enter in the sentence that you wish to enter:")

    return sentence

def sentenceSplit(sentences):
    newList = []
    newList = sentences.split(". " or ".")
    print(newList)

    return newList


def getVerfied(newList):

    trueList = False # Base boolean
    while not trueList:
        for i in range(len(newList)):
            firstWord = newlist.pop[i][0]
            print
            newList[i][0] = newList[i][0].upper()
            print(newList)
        
# Example!!!!!!!!!!!!
for i in range(len(InsertList)):
    blank variable=(Insertlist)[i].split()
    for word in words:

        words[0] = words[0].title()
        InsertList[i] = words
        print(words)



def capfirstWord(newList):
    for word in range(len(newList)):
        firstWord = newList[word]
        firstWord = firstWord.title()
        thingy = newList[word].split()
        print(firstWord)
        print(thingy)


# Can i do this? bruh fuck this shit! i can do this dumb ass fucking shit.
main()
