__author__ = 'vishrutreddi'

import requests
import xmltodict
import xml.etree.ElementTree as ET




def queryCreator(paperName, authorName, institutionName):

    baseURL = 'http://ieeexplore.ieee.org/gateway/ipsSearch.jsp?querytext='

    errorMssg = "-NONE-"
    warningMssg = "-NONE-"

    queryCase = -1

    paperNamePresent = False
    authorNamePresent = False
    institutionNamePresent = False

    # Check what all Search Names are entered by the user
    if(len(paperName) > 0):
        paperNamePresent = True

    if(len(authorName) > 0):
        authorNamePresent = True

    if(len(institutionName) > 0):
        institutionNamePresent = True

    query = ""

    # All 3 search terms are present
    if(paperNamePresent and authorNamePresent and institutionNamePresent):
        query = "(" + authorName + " OR "+ institutionName + ") AND \"Document Title\":" + paperName + "."
        warningMssg = "Search Results expected to be: VERY STRONG"

    elif(paperNamePresent and authorNamePresent):
        query = "(" + authorName + ") AND \"Document Title\":" + paperName + "."
        warningMssg = "Search Results expected to be: STRONG"

    elif(paperNamePresent and institutionNamePresent):
        query = "(" + institutionName + ") AND \"Document Title\":" + paperName + "."
        warningMssg = "Search Results expected to be: MEDIUM"

    elif(authorNamePresent and institutionNamePresent):
        query = "(" + authorName + " OR "+ institutionName + ") AND \"Document Title\":" + paperName + "."
        warningMssg = "Search Results expected to be: WEAK"

    elif(paperNamePresent):
        query = "\"Document Title\":" + paperName + "."
        warningMssg = "Search Results expected to be: MEDIUM"

    elif(authorNamePresent):
        query = authorName
        warningMssg = "Search Results expected to be: VERY WEAK"

    elif(institutionNamePresent):
        query = institutionName
        warningMssg = "Search Results expected to be: VERY WEAK"

    else:
        errorMssg = "Insufficient Data Provided. Unable to proceed with the process."

    finalURL = baseURL + query;

    print('\n WARNING: ' + warningMssg)
    print('ERROR:' + errorMssg)
    print('\n SEARCH URL: ' + finalURL +"\n");

    count = 20

    # Call to get and print Results
    data = getResults(finalURL, count)

    return data


def getResults(finalURL, count):


    sourceCode = requests.get(finalURL)
    xmlSource = sourceCode.text

    xmlObj = ET.fromstring(xmlSource)

    data = ""

    print(xmlObj)
    for child in xmlObj:
        print("" + str(child.tag) + ","  + str(child.attrib) + " => " + child.text)
        data += "<b>" + str(child.tag) + ":</b> " + child.text + "<br> <br>"
        for step_child in child:
                data += "<b>" + str(step_child.tag) + ":</b> " + step_child.text + "<br>"
                for step2_child in step_child:
                    data += "<b>" + str(step2_child.tag) + ":</b> " + step2_child.text + "<br>"


    return data


