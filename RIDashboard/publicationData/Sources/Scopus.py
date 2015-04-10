__author__ = 'vishrutreddi'





def searchURL(item):
    temp = "%28"+item.get_Values("Title").Replace(" ", "+")+"%29"
    baseURL = "https://www.scopus.com/results/results.url?sort=plf-f&src=s&sot=b&sdt=b&sl'"+(temp.length+1).toString()+"&s=TITLE"
    url = baseURL + temp
    return url



# METHOD 2 USING API KEY
'''
.....
....
...
'''

'''
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
    getResults(finalURL, count)



def getResults(finalURL, count):


    sourceCode = requests.get(finalURL)
    xmlSource = sourceCode.text

    xmlObj = ET.fromstring(xmlSource)

    print(xmlObj)
    for child in xmlObj:
        print("" + str(child.tag) + ","  + str(child.attrib) + " => " + child.text)
        for step_child in child:
                print("    " + str(step_child.tag) + ","  + str(step_child.attrib) + " => " + step_child.text)
                for step2_child in step_child:
                    print("    " + str(step2_child.tag) + ","  + str(step2_child.attrib) + " => " + step2_child.text)





queryCreator()
'''
