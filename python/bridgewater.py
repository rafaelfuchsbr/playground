#!/bin/python3

import math
import os
import random
import re
import sys



#
# Assumptions
# - Text is always in English, so only English scenarios are being considered (like punctuation, abbreviations, etc).
# - I got a list of common abbreviations. There should be more out there.
# - I'm considering contractions as one unique word. They won't be separate or expanded.
#
#  There is a scenario that I have not covered in the code as it would add a considerable complexity to the 
#  analysis and I'm not sure this is the goal of this exercise. The scenario is related to sentences or even
#  names/expressions with punctuation and/or surrounded by quotes. Examples:
#  * Watch "Jeopardy! ", Alex Trebek's fun TV quiz game.
#    -> In this example, the "!" will break the text into a separate sentence, which is not the case here.
#  * Quick, Baz, get my woven flax jodhpurs! "Now fax quiz Jack! " my brave ghost pled.
#    -> In this example, the "!" inside the quotes will break the text into a separate sentence. The text inside the
#       quotes is a sentence itself, but the text around it can be considered part of the same bigger sentence.
#
#  To consider these scenarios in the right way, I would need to check for balanced quotes and if the text inside
#  the quotes are sentences alone and if the text outside the quotes are separate sentences as well.
#
#  These examples were taken from a text generator so I could test bigger texts to take a look into performance.
#  This is the classic "The quick, brown fox jumps over a lazy dog." text.
#  https://www.blindtextgenerator.com/
#

import re

#gather the properties for each word and format in the desired format
def formatWordAndProperties(result, word):
    count = result[word]["count"]
    #cast integers (sentence numbers) to string and join them, separate by comma
    sentenceNumbers = ",".join(str(sentence) for sentence in result[word]["sentences"])
    #return the formatted line with the values
    #count and sentenceNumbers variables could be omitted and the assignments could happen 
    #   directly in the line below, but I like to code this way for improved readability
    return "%s: {%s:%s}" % (word, count, sentenceNumbers)

#process a single word
def processWord(result, word, trackedSpecialWords, sentenceNumber):
    specialChars = ',:;-\'"@#$%&*+=(){}\<>[]/'

    #if the word start with ^ it means it's a tracked special word
    if word.startswith("^"):
        #get the string related to the placeholder for the special word
        word = trackedSpecialWords[int(word[1:])]
    else: 
        #if we are here, then it's a simple regular word
        #remove any special char that may be in the start.end of the word
        word = word.strip(specialChars)
        
    #if empty string we don't need to track the word
    # if it's only special char, then it's not a word as well
    if word == "" or word == " ":
        return
    
    if word not in result:
        #if first appeareance, the we need to initialize the data
        result[word] = { "count" : 0, "sentences": [] }
    
    result[word]["count"] += 1
    #append sentence number, even it's repeated
    result[word]["sentences"].append(sentenceNumber)  
    
def identifySpecialWords(fullText, trackedSpecialWords):
    #this method will identify special words, which have to be handled in a different way
    #this is specially true for abbreviations which contain dots - avoid splitting these words into separate sentences
    #regular expression to identify abbreviations and chars joined by dots, like i.e., e.g., x.y.z
    specialWordsPattern = "\\b(?:[a-zA-Z]\\.){2,}"
    #common English abbreviations
    preDefinedSpecialWords = ["mr.", "mrs.", "ms.","dr.","rev.","sen.","prof.","hon.","st.","capt.","gen.","etc.","et al.","ca.","sc.","viz.","v.","cf."]
        
    #get special words using the regular expression
    specialWords = re.findall(specialWordsPattern, fullText)
    specialWords = specialWords + preDefinedSpecialWords
    
    specialIndex = 0
    for specialWord in specialWords:
        if specialWord in fullText:
            #if the special words in present, define a plaholder with an index like ^1, ^2, etc
            placeholder = "^"+str(specialIndex)   
            #replace the atual word by its placeholder       
            fullText = fullText.replace(specialWord, placeholder)
            #add the special word to the trscked words array so we can retrive them later using the index in the placeholder
            trackedSpecialWords.append(specialWord)
            specialIndex += 1 
    
    #return the fulltext with placeholder as we changed the reference of the object
    return fullText

def processSentences(fullText, trackedSpecialWords):
    #split text by punctuation marks
    sentences = re.split("\.|\?|\!", fullText)
    #result will contain the list of words and the properties with are gathering - number of occurrences and list of sentences where they appear
    result = {}
    for index,sentence in enumerate(sentences):
        #iterate sentencesand split them by space to identify the words
        words = sentence.split(" ")
        for word in words:
            processWord(result, word, trackedSpecialWords, index+1)

    return result

def printResult(result):
    #order the list of words so we have them in alphabetical order
    orderedResults = sorted(result)
    for word in orderedResults:
        print(formatWordAndProperties(result, word))
    
def generateAndPrintConcordance(inputLines):
    #variable to store the special words we will be tracking
    trackedSpecialWords = []
    #join all lines and make all words lower case and we don't care about the case
    fullText = " ".join(inputLines).lower()
    #check text for special words and store them in trackedSpecialWords
    fullText = identifySpecialWords(fullText, trackedSpecialWords)
    #process text and each sentence to generate the statistics we are looking for
    result = processSentences(fullText, trackedSpecialWords)
    #print the data from the sentences analysis
    printResult(result)
            
        
        
if __name__ == '__main__':
    inputLines_count = int(input().strip())

    inputLines = []

    for _ in range(inputLines_count):
        inputLines_item = input()
        inputLines.append(inputLines_item)

    generateAndPrintConcordance(inputLines)
