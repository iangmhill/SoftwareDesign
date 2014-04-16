# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 11:10:37 2014

@author: ihill
"""
from re import findall

files = [
        ['1726','1729'],
        ['1812','1813'],
        ['1820','1823'],
        ['1837','1838'],
        ['1843','1847'],
        ['1851','1852','1859'],
        ['1865','1869'],
        ['1873','1874','1876'],
        ['1883','1884','1887'],
        ['1892','1895','1897'],
        ['1900','1902','1908','1911']
        ]
        
commonWords = ['the','and','to','i','a','it','of','in','she','you','that','was','her','but','be','as','with']
# she and her made the cut but not he or his?

def stripBoilerPlate(book):
    """
    Takes a large string containing a book from Project Gutenberg and removes
    the unrelated information at the top and bottom of the string.
    Returns a string with the boilerplate removed.
    """
    beginning = book.find(' ***')+4   #Find the end of extra information at the beginning
    end = book.find('*** END OF')     #Find the start of the extra information at the end
    return book[beginning : end]      #Return only the actual book

def filePreparation(files):
    """
    Uses the stripBoilerPlate(book) function to clean each file in the two
    layer deep list given to the function.
    The function produces no output in python, but creates a new file
    with the suffix "x.txt" that only contains the actual book.
    This function was created so that the stripping of the boilerplate
    needs to only happen once and not every time the program is run.
    """
    for n in range(len(files)):                  #search through each time period
        for m in range(len(files[n])):           #prepare each book in this time period                  
            f = open(files[n][m] + '.txt','r')   #open the file downloaded from Project Gutenberg and prepare to read
            b = open(files[n][m] + 'x.txt','w')  #create a new file for only the book and prepare to write to the file
            raw_file = f.read()
            book = stripBoilerPlate(raw_file)    
            b.write(stripBoilerPlate(book))      #write the book to the new file
            f.close()                            #clean up
            b.close()
            
def findWords(filename):
    """
    Opens a file with the given filename and separates the words into a list.
    Returns a list of the words in the file
    """
    b = open(filename,'r')             #Open the file for reading
    book = b.read()
    words = findall("[a-zA-Z']+",book) #Find all words that contain letters and apostrophes
    b.close()                          #clean up
    for w in range(len(words)):        #clean the word list
        words[w] = words[w].lower()    #make everything lowercase to allow for easier analysis
        if words[w][-2:] == "'s":      #if the word ends with an "'s" get rid of the "'s"
            words[w] = words[w][:-2]
    return words                       #return the list of words

def wordFrequency(words):
    """
    Given a list of words, wordFrequency() will return a dictionary containing
    the frequency of the words in the list.
    """
    freq = {}              #initialize dictionary
    for w in words:
        if w in freq:      #if the word already exists in the dictionary increase the value by 1
            freq[w] += 1
        else:              #if the word does not already exist, create a new key for it and assign it the value of 1
            freq[w] = 1
    return freq            #return the dictionary

def sortDescending(dictionary):
    """
    Takes a dictionary and returns a list of tuples sorted by value
    """
    sorted_ascending = sorted(dictionary.items(), key=lambda x:x[1])                     #sorted function returns list in ascending order
    sorted_descending = [sorted_ascending[-x] for x in range(1,len(sorted_ascending)+1)] #list comprehension recreates the list in descending order
    return sorted_descending

def scaleToPercentage(d):
    """
    Takes a dictionary with keys and values and  scales the 
    values around the combined total of all values
    """
    total = sum(d.values())
    for k,v in d.iteritems():
        d[k] = v/float(total)
    return d

def calculateDictionaryDistance(standard, dictionary):
    different = 0
    same = 0
    offset = 0
    for k in standard:
        if k in dictionary:
            offset += abs(standard[k] - dictionary[k])
            same += 1
        else:
            different += 1
    for k in dictionary:
        if not k in standard:
            different += 1
    difference = different/float(same+different)
    return [offset, difference]
        


#---------------------------- Preparation Code ----------------------------#
"""
Only needs to be run once!
"""

#filePreparation(files)

#------------------------------ Main Program ------------------------------#

# It would be good practice in future to wrap this in an if __name__=="__main__":

books = []
booksInThisPeriod = []
for n in range(len(files)):                  #search through each time period
    for m in range(len(files[n])):           #parse each book in this time period                  
        words = findWords(files[n][m]+'x.txt')
        freq = wordFrequency(words)
        print("Frequency dictionary calculated: " + files[n][m] +'x.txt')
        booksInThisPeriod.append(freq)
    books.append(booksInThisPeriod)
    booksInThisPeriod = []
"""
Combine dictionaries from each time period to create a scaled
representative dictionary for each time period
"""

representative = []
for n in range(len(files)):
    z = {}
    for m in range(len(files[n])):
        for k in books[n][m]:
            if k in z:      #if the word already exists in the dictionary increase the value by 1
                z[k] += books[n][m][k]
            else:              #if the word does not already exist, create a new key for it and assign it the value of 1
                z[k] = books[n][m][k]
    print("Dictionary merged: " + files[n][0][:-1] + "0 contains " + str(sum(z.values())) + " words")
    representative.append(scaleToPercentage(z))
print("Number of time periods to be analyzed: " + str(len(representative)))

"""
Compare the word counts of time period to a standard time period
"""
standard = representative[-6]   #the most recent era is the standard
for n in range(len(representative)):
    result = calculateDictionaryDistance(standard,representative[n])
    print(files[n][0][:-1] + "0:")
    print("        Offset: " + str(result[0]))
    print("        % of words different: " + str(result[1]))