__author__ = 'vishrutreddi'


import requests
import xmltodict
import xml.etree.ElementTree as ET
from xml.dom import minidom


'''
Check the API. Key is Needed.

PLOS API KEY: Kwz99bX_84vY--bErMfU
(Can be used both for their Search API and also for their ALM API)
'''

# Description: This method creates the query links for PLOS API request and the result the URL spit out
#			   is XML Data. THis method then parses that data and creates a huge HTML string and returns 
# 			   that string so that it cna be presented on the RIDashboard Web-APp.
#
# @param authorName - Name of the Author/Researcher
# @param institutionName - Name of the institution the author is affiliated with
#
# @return data - HTML data with researcher publication data from PLOS
def getPLOSData(authorName, institutionName):

    authorNamePresent = False
    institutionNamePresent = False

    query1 = ''
    query2 = ''

    if(len(institutionName) > 0):
        institutionNamePresent = True;

    if(len(authorName) > 0):
        authorNamePresent = True;

    if(institutionNamePresent == True and authorNamePresent == True):
        query1 = 'http://api.plos.org/search?q=' + authorName + ' ' + institutionName + '&api_key=Kwz99bX_84vY--bErMfU'

    elif(authorNamePresent == True and institutionNamePresent == False):
        #query1 = 'http://api.plos.org/search?q=author:"' + authorName + '"&api_key=Kwz99bX_84vY--bErMfU'
        query1 = 'http://api.plos.org/search?q=' + authorName + '&api_key=Kwz99bX_84vY--bErMfU'


    else:
        return 'No Result Possible. Invalid Inputs or no results produced from PLOS.'

    print(query1);
    # Call to get and print Results
    data = getResults(query1)

    return data


def getResults(query):

    #Article Data
    title = []
    authors = []
    plosScore = []
    abstract = []
    py = []
    articleType = []

    titleSeeen = False;
    authorsSeen = False;
    plosScoreSeen = False;
    abstractSeen = False;
    pySeen = False;
    articleTypeSeen = False;

    sourceCode = requests.get(query)
    xmlSource = sourceCode.text
    xmlObj = ET.fromstring(xmlSource)

    for child in xmlObj:

        if child.tag == 'result':

            for subChild in child:

                if subChild.tag == 'doc':

                    titleSeeen = False;
                    authorsSeen = False;
                    plosScoreSeen = False;
                    abstractSeen = False;
                    pySeen = False;
                    articleTypeSeen = False;

                    for newBorn in subChild:

                        # Publication Date
                        if newBorn.tag == 'date':
                            pySeen = True;
                            py.append(newBorn.text);

                        # Authors
                        elif newBorn.tag == 'arr' and newBorn.attrib['name'] == 'author_display':
                            authorsSeen = True;
                            data = '' 
                            for cell in newBorn:
                                data += cell.text + '; '

                            authors.append(data);

                        # Title
                        elif newBorn.tag == 'str' and newBorn.attrib['name'] == 'title_display':
                            titleSeeen = True;
                            title.append(newBorn.text);

                        # PLOS Score
                        elif newBorn.tag == 'float':
                            plosScoreSeen = True;
                            plosScore.append(newBorn.text);

                        # Abstract
                        elif newBorn.tag == 'arr' and newBorn.attrib['name'] == 'abstract':
                            abstractSeen = True;
                            for cell in newBorn:
                                abstract.append(cell.text);

                        # Article Type
                        elif newBorn.tag == 'str' and newBorn.attrib['name'] == 'article_type':
                            articleTypeSeen = True;
                            articleType.append(newBorn.text);


                    if titleSeeen == False:
                        title.append("-NONE-");

                    if authorsSeen == False:
                        authors.append("-NONE-");

                    if plosScoreSeen == False:
                        plosScore.append("-NONE-");

                    if abstractSeen == False:
                        abstract.append("-NONE-");

                    if pySeen == False:
                        py.append("-NONE-");

                    if articleTypeSeen == False:
                        articleType.append("-NONE-");




    PLOSData = {
                    'title' : title,
                    'authors' : authors,
                    'py' : py,
                    'articleType' : articleType,
                    'plosScore' : plosScore,
                    'abstract' : abstract
                }


    return PLOSData



