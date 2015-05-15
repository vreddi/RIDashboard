__author__ = 'vishrutreddi'

import requests
import xmltodict
import xml.etree.ElementTree as ET


def getIEEEData(authorName, institutionName):  

    paperNamePresent = False
    authorNamePresent = False
    institutionNamePresent = False

    if(len(institutionName) > 0):
        institutionNamePresent = True;

    if(len(authorName) > 0):
        authorNamePresent = True;

    if(institutionNamePresent == True and authorNamePresent == True):
        query = 'http://ieeexplore.ieee.org/gateway/ipsSearch.jsp?querytext=' + institutionName + '&au=' + authorName + '&hc=1000&rs=1&sortfield=ti&sortorder=asc'

    elif(authorNamePresent == True and institutionNamePresent == False):
        query = 'http://ieeexplore.ieee.org/gateway/ipsSearch.jsp?&au=' + authorName + '&hc=1000&rs=1&sortfield=ti&sortorder=asc'

    else:
        return 'No Result Possible. Invalid Inputs or no results produced from IEEE Explorer.'

    print('URL: ' + query);

    # Call to get and print Results
    data = getResults(query)

    return data


def getResults(query):


    # Article Data
    title = []
    authors = []
    affiliations = []
    controlledterms = []
    thesaurusterms = []
    pubtitle = []
    punumber = []
    pubtype = []
    publisher = []
    py = []
    spage = []
    epage = []
    abstract = []
    isbn = []
    htmlFlag = []
    arnumber = []
    publicationId = []
    partnum = []
    mdurl = []
    pdf = []

    sourceCode = requests.get(query)
    xmlSource = sourceCode.text

    xmlObj = ET.fromstring(xmlSource)

    data = ""

    titleSeen = False;
    authorsSeen = False;
    affiliationSeen = False;
    controlledtermsSeen = False;
    thesaurustermsSeen = False;
    pubtitleSeen = False;
    punumberSeen = False;
    pubtypeSeen = False;
    publisherSeen = False;
    pySeen = False;
    spageSeen = False;
    epageSeen = False;
    isbnSeen = False;
    abstractSeen = False
    htmlFlagSeen = False
    partnumSeen = False;
    publicationIdSeen = False;
    mdurlSeen = False;
    arnumberSeen = False;
    pdfSeen = False;

    for child in xmlObj:

        if child.tag == 'document':

            titleSeen = False;
            authorsSeen = False;
            affiliationSeen = False;
            controlledtermsSeen = False;
            thesaurustermsSeen = False;
            pubtitleSeen = False;
            punumberSeen = False;
            pubtypeSeen = False;
            publisherSeen = False;
            pySeen = False;
            spageSeen = False;
            epageSeen = False;
            isbnSeen = False;
            abstractSeen = False
            htmlFlagSeen = False
            partnumSeen = False;
            publicationIdSeen = False;
            arnumberSeen = False;
            mdurlSeen = False;
            pdfSeen = False;


            for subChild in child:

                if subChild.tag == 'title':
                    titleSeen = True;
                    if len(subChild.text) == 0:
                        title.append("-NONE-");
                    else:
                        title.append(subChild.text);

                elif subChild.tag == 'authors':
                    authorsSeen = True;
                    if len(subChild.text) == 0:
                        authors.append("-NONE-");
                    else:
                        authors.append(subChild.text);

                elif subChild.tag == 'affiliations':
                    affiliationSeen = True;
                    if len(subChild.text) == 0:
                        affiliations.append("-NONE-");
                    else:
                        affiliations.append(subChild.text);

                elif subChild.tag == 'controlledterms':
                    controlledtermsSeen = True;
                    terms = [];
                    if len(subChild.text) == 0:
                        controlledterms.append("-NONE-");
                    else:
                        for newBorn in subChild:
                            terms.append(newBorn.text);

                        controlledterms.append(terms);

                elif subChild.tag == 'thesaurusterms':
                    thesaurustermsSeen = True;
                    terms = [];
                    if len(subChild.text) == 0:
                        thesaurusterms.append("-NONE-");
                    else:
                        for newBorn in subChild:
                            thesaurusterms.append(newBorn.text);

                        thesaurusterms.append(terms);

                elif subChild.tag == 'pubtitle':
                    pubtitleSeen = True;
                    if len(subChild.text) == 0:
                        pubtitle.append("-NONE-");
                    else:
                        pubtitle.append(subChild.text);

                elif subChild.tag == 'punumber':
                    punumberSeen = True;
                    if len(subChild.text) == 0:
                        punumber.append("-NONE-");
                    else:
                        punumber.append(subChild.text);

                elif subChild.tag == 'pubtype':
                    pubtypeSeen = True;
                    if len(subChild.text) == 0:
                        pubtype.append("-NONE-");
                    else:
                        pubtype.append(subChild.text);

                elif subChild.tag == 'publisher':
                    publisherSeen = True;
                    if len(subChild.text) == 0:
                        publisher.append("-NONE-");
                    else:
                        publisher.append(subChild.text);

                elif subChild.tag == 'py':
                    pySeen = True;
                    if len(subChild.text) == 0:
                        py.append("-NONE-");
                    else:
                        py.append(subChild.text);

                elif subChild.tag == 'spage':
                    spageSeen = True;
                    if len(subChild.text) == 0:
                        spage.append("-NONE-");
                    else:
                        spage.append(subChild.text);

                elif subChild.tag == 'epage':
                    epageSeen = True;
                    if len(subChild.text) == 0:
                        epage.append("-NONE-");
                    else:
                        epage.append(subChild.text);

                elif subChild.tag == 'abstract':
                    abstractSeen = True;
                    if len(subChild.text) == 0:
                        abstractSeen.append("-NONE-");
                    else:
                        abstract.append(subChild.text);

                elif subChild.tag == 'isbn':
                    isbnSeen = True;
                    if len(subChild.text) == 0:
                        isbn.append("-NONE-");
                    else:
                        isbn.append(subChild.text);

                elif subChild.tag == 'htmlFlag':
                    htmlFlagSeen = True;
                    if len(subChild.text) == 0:
                        htmlFlag.append("-NONE-");
                    else:
                        htmlFlag.append(subChild.text);

                elif subChild.tag == 'arnumber':
                    arnumberSeen = True;
                    if len(subChild.text) == 0:
                        arnumber.append("-NONE-");
                    else:
                        arnumber.append(subChild.text);

                elif subChild.tag == 'publicationId':
                    publicationIdSeen = True;
                    if len(subChild.text) == 0:
                        publicationId.append("-NONE-");
                    else:
                        publicationId.append(subChild.text);

                elif subChild.tag == 'partnum':
                    partnumSeen = True;
                    if len(subChild.text) == 0:
                        partnum.append("-NONE-");
                    else:
                        partnum.append(subChild.text);

                elif subChild.tag == 'mdurl':
                    mdurlSeen = True;
                    if len(subChild.text) == 0:
                        mdurl.append("-NONE-");
                    else:
                        mdurl.append(subChild.text);

                elif subChild.tag == 'pdf':
                    pdfSeen = True;
                    if len(subChild.text) == 0:
                        pdf.append("-NONE-");
                    else:
                        pdf.append(subChild.text);
            


            if titleSeen == False:
                title.append("-NONE-");

            if authorsSeen == False:
                authors.append("-NONE-");

            if affiliationSeen == False:
                affiliations.append("-NONE-");

            if controlledtermsSeen == False:
                controlledterms.append("-NONE-");

            if thesaurustermsSeen == False:
                thesaurusterms.append("-NONE-");

            if pubtitleSeen == False:
                pubtitle.append("-NONE-");

            if punumberSeen == False:
                punumber.append("-NONE-");

            if pubtypeSeen == False:
                pubtype.append("-NONE-");

            if publisherSeen == False:
                publisher.append("-NONE-");

            if pySeen == False:
                py.append("-NONE-");

            if spageSeen == False:
                spage.append("-NONE-");

            if epageSeen == False:
                epage.append("-NONE");

            if isbnSeen == False:
                isbn.append("-NONE-");

            if abstractSeen == False:
                abstract.append("-NONE-");

            if htmlFlagSeen == False:
                htmlFlag.append("-NONE-");

            if partnumSeen == False:
                partnum.append('-NONE-');

            if publicationIdSeen == False:
                publicationId.append("-NONE-");

            if mdurlSeen == False:
                mdurl.append("-NONE-");

            if pdfSeen == False:
                pdf.append("-NONE-");

            if arnumberSeen == False:
                arnumber.append("-NONE");

    # Create the Dictionary
    IEEEData = {
                    'title' : title, 
                    'authors' : authors, 
                    'affiliations' : affiliations, 
                    'controlledterms' : controlledterms,
                    'thesaurusterms' : thesaurusterms,
                    'pubtitle' : pubtitle,
                    'punumber' : punumber,
                    'pubtype' : pubtype,
                    'publisher' : publisher,
                    'py' : py,
                    'spage' : spage,
                    'epage' : epage,
                    'abstract' : abstract,
                    'isbn' : isbn,
                    'htmlFlag' : htmlFlag,
                    'arnumber' : arnumber,
                    'publicationId' : publicationId,
                    'partnum' : partnum,
                    'mdurl' : mdurl,
                    'pdf' : pdf
                };

    return IEEEData


