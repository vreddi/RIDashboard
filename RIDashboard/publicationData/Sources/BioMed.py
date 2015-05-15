__author__ = 'vishrutreddi'

from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import json
import urllib.request
import requests


def getBioMedData(authorName, institutionName):

    # Partition into words and remove punctuation marks
    # tokenizer = RegexpTokenizer(r'\w+')
    # words = tokenizer.tokenize(paperName)

    # Removing Stop Words
    # words_without_stopwords = []

    # stop = stopwords.words('english')

    # # Add in non stop-words
    # for word in words:
    #     if(word not in stop):
    #         words_without_stopwords.append(word)

    if(len(authorName) == 0 and len(institutionName) == 0):
        return 'No Result Possible. Invalid Inputs or no results produced from BioMed.';

    query = authorName + " " + institutionName;

    baseURL = 'http://www.biomedcentral.com/search/results?terms='

    queryURL = baseURL + query

    formatJsonURL = queryURL + '&format=json'


    # Final URL Created for the API Call
    finalURL = formatJsonURL

    print(finalURL)

    r = requests.get(finalURL)

    jsonURLData = r.json()

    print(str(jsonURLData))
    print(finalURL)
    resultCounter = 1


    title = []
    authors = []
    py = []
    citation = []
    abstractPath = []
    articleType = []

    if(len(jsonURLData['entries']) > 1):
        for dataUnit in jsonURLData['entries']:

            py.append(dataUnit['published Date']);

            title.append(dataUnit['bibliograhyTitle']);

            abstractPath.append(dataUnit['abstractPath']);

            articleType.append(dataUnit['type']);

            authors.append(dataUnit['authorNames']);

            
        BioMedData = {

            'title' : title,
            'authors' : authors,
            'py' : py,
            'citation' : citation,
            'abstractPath' : abstractPath,
            'articleType' : articleType
        }

    return BioMedData