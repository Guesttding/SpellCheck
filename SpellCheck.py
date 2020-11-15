def ED(first, second):
    """Returns the edit distance between the strings first and second"""
    # if first is an empty string (how do we write an empty string in python?)
        # return the length of the string second
    # elif second is an empty string (how do we write an empty string in python?)
        # return the length of the string second
    # elif the first letter in first is equal to the first letter in second
        return ED(first[1:], second[1:])
    else:
        substitution = 1 + ED(first[1:], second[1:])
        deletion = 1 + ED(first[1:], second)
        insertion = 1 + ED(first, second[1:])
        # compare substitution, deletion, and insertion (which are all numbers) and return the smallest one
        # hint: google the "minimum" function for python

def fastED(S1, S2, memo):
    """Returns the edit distance between the strings first and second using a memo"""
    if (S1, S2) in memo:
        return memo[(S1, S2)]
    # elif S1 is an empty string (how do we write an empty string in python?)
        # create a variable called answer and give it the length of S2
     # elif S2 is an empty string (how do we write an empty string in python?)
        # create a variable called answer and give it the length of S1
     # elif the first letter in S1 is equal to the first letter in S2
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

def spam():
    """Prompts the user for an input word and returns Correct if the word is in the master list or the 10 most similar words if the word is not in the master list"""
    
    # open "sampleDictonary.txt" and save it in a file named f
    # read f and save it in a variable called contents

    words = contents.split("\n")
    
    # create a variable called startTime and have it keep track of when time started
    # hint: Google "how to start counting time in python"

    userInput = input("spell check> ")
    
    if userInput in words:
        # return the word "Correct" if the user input is in words
    else:
        # print "Suggested alternatives:" 
        
        memo = {}
        tupleList = list(map(lambda x : (fastED(userInput, words[x], memo), words[x]), range(len(words))))
        tupleList.sort()
        topList = [tupleList[x][1] for x in range(10)]
        topList.sort()
        [print(topList[x]) for x in range(len(topList))]
    
    # create a variable called endTime and have it keep track of when time ended
    print("Computation time:", endTime - startTime, "seconds")