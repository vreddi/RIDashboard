__author__ = 'vishrutreddi'

from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import json
import urllib.request


def searchBioMed():

    paperName = input('Enter Research Paper Name: ')
    authorName = input('Enter Author(s) Name: ')
    institutionName = input('Enter Affiliated Institution: ')

    # Partition into words and remove punctuation marks
    tokenizer = RegexpTokenizer(r'\w+')
    words = tokenizer.tokenize(paperName)

    # Removing Stop Words
    words_without_stopwords = []

    stop = stopwords.words('english')

    # Add in non stop-words
    for word in words:
        if(word not in stop):
            words_without_stopwords.append(word)

    query = " ".join(words)

    baseURL = 'http://www.biomedcentral.com/search/results?terms='

    queryURL = baseURL + query

    formatJsonURL = queryURL + '&format=json'


    # Final URL Created for the API Call
    finalURL = formatJsonURL

    print(finalURL)

    with urllib.request.urlopen(finalURL) as jsonData:
        raw = jsonData.read()
        jsonURLData = json.loads(raw.decode())

    print(str(jsonURLData))
    print(finalURL)
    resultCounter = 1

    for dataUnit in jsonURLData['entries']:

        print('RESULT ' + str(resultCounter) + ': ')
        print('--------------------------------------------------------------------------------------')
        print('Published Date: ' + dataUnit['published Date'])
        print('Title: ' + dataUnit['bibliograhyTitle'])
        print('Data-Type: ' + dataUnit['type'])
        print('Citation Data: ' + dataUnit['longCitation'])
        print('Abstract URL Path: ' + dataUnit['abstractPath'])
        resultCounter += 1


        print('\n')


#Call the main Function
#For Testing
searchBioMed()