import time
def ED(first, second):
    """Returns the edit distance between the strings first and second"""
    if first == '': 
      return len(second)
    elif second == '':
      return len(first)
    elif first[0] == second[0]:
        return ED(first[1:], second[1:])
    else:
        substitution = 1 + ED(first[1:], second[1:])
        deletion = 1 + ED(first[1:], second)
        insertion = 1 + ED(first, second[1:])
        return min(substitution,deletion,insertion)

def fastED(S1, S2, memo):
    """Returns the edit distance between the strings first and second using a memo"""
    if (S1, S2) in memo:
        return memo[(S1, S2)]
    elif S1=="":
        return len(S2)
    elif S2=="":
        return len(S1)
    
    elif S1[0]==S2[0]:
        answer = fastED(S1[1:], S2[1:], memo)
    else:
        substitution = 1 + fastED(S1[1:], S2[1:], memo)
        deletion = 1 + fastED(S1[1:], S2, memo)
        insertion = 1 + fastED(S1, S2[1:], memo)
        answer = min(substitution, deletion, insertion)
    memo[(S1, S2)] = answer
    return answer

def topNmatches(word, nummatches, ListOfWords):
    """Returns the alpabetically-sorted list of a total of nummatches words from ListOfWords that have the lowest edit-distance scores with the input word"""
    tupleList = list(map(lambda x : (fastED(word, ListOfWords[x], {}), ListOfWords[x]), range(len(ListOfWords))))
    tupleList.sort()
    topList = [tupleList[x][1] for x in range(nummatches)]
    topList.sort()
    return topList

import time

def spellChecker():
    """Prompts the user for an input word and returns Correct if the word is in the master list or the 10 most similar words if the word is not in the master list"""
    
    # open "sampleDictonary.txt" and save it in a file named f
    with open("sampleDictionary.txt","r")as f:
    # read f and save it in a variable called contents
        contents = f.read()

        words = contents.split("\n")
    
        startTime=time.time()

        userInput = input("spell check> ")
    
    if userInput in words:
        return print("Correct")
    else:
        # print "Suggested alternatives:" 
        print("Suggested alternatives:")
        memo = {}
        tupleList = list(map(lambda x : (fastED(userInput, words[x], memo), words[x]), range(len(words))))
        tupleList.sort()
        topList = [tupleList[x][1] for x in range(10)]
        topList.sort()
        [print(topList[x]) for x in range(len(topList))]
    endTime=time.time()
    
    # create a variable called endTime and have it keep track of when time ended
    print("Computation time:", endTime - startTime, "seconds")

spellChecker()


