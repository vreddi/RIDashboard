__author__ = 'vishrutreddi'

import requests
import xmltodict
import xml.etree.ElementTree as ET
import re


def getArvixData(authorName, institutionName):  

    authorNamePresent = False
    institutionNamePresent = False

    if(len(institutionName) > 0):
        institutionNamePresent = True;

    if(len(authorName) > 0):
        authorNamePresent = True;

    if(institutionNamePresent == True and authorNamePresent == True):
        query = 'http://export.arxiv.org/api/query?search_query=' + authorName + ' ' + institutionName + '&start=0&max_results=25'

    elif(authorNamePresent == True and institutionNamePresent == False):
        query = 'http://export.arxiv.org/api/query?search_query=' + authorName + '&start=0&max_results=25'

    else:
        return 'No Result Possible. Invalid Inputs or no results produced from Arvix.'

    print('URL: ' + query);

    # Call to get and print Results
    data = getResults(query)

    return data


def getResults(query):


    # Article Data
    title = []
    authors = []
    affiliations = []
    abstract = []
    py = []

    sourceCode = requests.get(query)
    xmlSource = sourceCode.text

    xmlObj = ET.fromstring(xmlSource)

    titleSeen = False;
    authorsSeen = False;
    affiliationSeen = False;
    pySeen = False;
    abstractSeen = False;

    for child in xmlObj:

        if re.sub(r'\{.*?\}', '', child.tag)  == 'entry':

        	titleSeen = False;
        	authorsSeen = False;
        	affiliationSeen = False;
        	pySeen = False;
        	abstractSeen = False;
        	authorStr = ''
        	affiliationStr = ''

        	for subChild in child:

        		realSubChild = re.sub(r'\{.*?\}', '', subChild.tag)

        		# Title
        		if realSubChild == 'title':
        			titleSeen = True;
        			title.append(subChild.text)

        		# Abstract
        		elif realSubChild == 'summary':
        			abstractSeen = True;
        			abstract.append(subChild.text);

        		# Publication Date
        		elif realSubChild == 'published':
        			pySeen = True;
        			py.append(subChild.text);

        		# Author and Affiliation
        		elif realSubChild == 'author':
        			for newBorn in subChild:

        				realNewBorn = re.sub(r'\{.*?\}', '', newBorn.tag);


        				if realNewBorn == 'name':
        					authorsSeen = True;
        					authorStr += newBorn.text + '; ';

        				elif realNewBorn == 'affiliation':
        					affiliationSeen = True;
        					affiliationStr += newBorn.text + '; ';


        	if(len(authorStr) > 0):
        		authors.append(authorStr);

        	if(len(affiliationStr) > 0):
        		affiliations.append(affiliationStr);

        	if titleSeen == False:
        		title.append("-NONE-");

        	if authorsSeen == False:
        		authors.append("-NONE-");

        	if affiliationSeen == False:
        		affiliations.append("-NONE-");

        	if abstractSeen == False:
        		abstract.append("-NONE-");

        	if pySeen == False:
        		py.append("-NONE-");

            

    # Create the Dictionary
    ArvixData = {
                    'title' : title, 
                    'authors' : authors, 
                    'affiliations' : affiliations, 
                    'py' : py,
                    'abstract' : abstract

                };

    return ArvixData


