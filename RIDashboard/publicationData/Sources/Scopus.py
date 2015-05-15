__author__ = 'vishrutreddi'

# # SCOPUS API KEY: 19b4b3546222699157deac547bc8e232

import requests
import json
import urllib.request
import requests


# # def getScopusIDs(MY_API_KEY):

# #     resp = requests.get("http://api.elsevier.com/content/search/scopus?query=AU-ID(7004212771)&field=dc:identifier&count=100",
# #                     headers={'Accept':'application/json',
# #                              'X-ELS-APIKey': MY_API_KEY})

# #     results = resp.json()
# #     return [[str(r['dc:identifier'])] for r in results['search-results']["entry"]]


# def get_scopus_info(SCOPUS_ID):
#     url = ("http://api.elsevier.com/content/abstract/scopus_id/"
#           + SCOPUS_ID
#           + "?field=authors,title,publicationName,volume,issueIdentifier,"
#           + "prism:pageRange,coverDate,article-number,doi,citedby-count,prism:aggregationType")
#     resp = requests.get(url,
#                     headers={'Accept':'application/json',
#                              'X-ELS-APIKey': '19b4b3546222699157deac547bc8e232'}) 

#     data = ""


#     print('\n')
#     results = json.loads(resp.text.encode('utf-8'))
#     #print(resp.text)
#     print('\n')

#     data += '<br><b>RESULT: <br> '
#     data += '-------------------------------------------------------------------------</b><br>'

#     print('Title: ' + str(results['abstracts-retrieval-response']['coredata']['dc:title'].encode('utf-8')))
#     data += '<b>Title: </b>' + str(results['abstracts-retrieval-response']['coredata']['dc:title'].encode('utf-8')) + '<br>'

#     print('Publication-Name: ' + str(results['abstracts-retrieval-response']['coredata']['prism:publicationName'].encode('utf-8')))
#     data += '<b>Publication-Name:</b> ' + str(results['abstracts-retrieval-response']['coredata']['prism:publicationName'].encode('utf-8')) + "<br>"

#     print('Cover-Date: ' + str(results['abstracts-retrieval-response']['coredata']['prism:coverDate'].encode('utf-8')))
#     data += '<b>Cover-Date: </b>' + str(results['abstracts-retrieval-response']['coredata']['prism:coverDate'].encode('utf-8')) + "<br>"

#     print('Citation: ' + str(results['abstracts-retrieval-response']['coredata']['citedby-count'].encode('utf-8')))
#     data += '<b>Citation: </b>' + str(results['abstracts-retrieval-response']['coredata']['citedby-count'].encode('utf-8')) + "<br>"

#     print('\n')

#     return data

# API_KEY = '19b4b3546222699157deac547bc8e232'
# get_scopus_info('SCOPUS_ID:0037368024')
# get_scopus_info('SCOPUS_ID:84898934670')
# get_scopus_info('SCOPUS_ID:84872864754')
# get_scopus_info('SCOPUS_ID:84876703352')
# get_scopus_info('SCOPUS_ID:80051860134')
# get_scopus_info('SCOPUS_ID:80051809046')
# get_scopus_info('SCOPUS_ID:79953651013') 

#     # fstring = '{authors}, {title}, {journal}, {volume}, {articlenum}, ({date}). {doi} (cited {cites} times).\n'
#     # return fstring.format(authors=', '.join([au['ce:indexed-name'] for au in results['abstracts-retrieval-response']['authors']['author']]),
#     #                       title=results['abstracts-retrieval-response']['coredata']['dc:title'].encode('utf-8'),
#     #                       journal=results['abstracts-retrieval-response']['coredata']['prism:publicationName'].encode('utf-8'),
#     #                       volume=results['abstracts-retrieval-response']['coredata']['prism:volume'].encode('utf-8'),
#     #                       articlenum=(results['abstracts-retrieval-response']['coredata'].get('prism:pageRange') or
#     #                           results['abstracts-retrieval-response']['coredata'].get('article-number')).encode('utf-8'),
#     #                       date=results['abstracts-retrieval-response']['coredata']['prism:coverDate'].encode('utf-8'),
#     #                       doi='doi:' + results['abstracts-retrieval-response']['coredata']['prism:doi'].encode('utf-8'),
#     #                       cites=int(results['abstracts-retrieval-response']['coredata']['citedby-count'].encode('utf-8')))



def get_scopus_info(query):

    print('Search Term(s): ' + query)

    finalURL = 'http://api.elsevier.com/content/search/index:SCOPUS?query=' + query + '&apiKey=19b4b3546222699157deac547bc8e232&httpAccept=application/json'

    data = ''

    r = requests.get(finalURL)

    jsonURLData = r.json()

    if(len(query) > 3):

        data += "</b>"
        for entry in jsonURLData['search-results']['entry']:

            data += '<b>Title: </b>' + entry['dc:title']
            data += '<br>'
            data += '<b>Citation Count: </b>' + entry['citedby-count']
            data += '<br>'
            data += '<br>'

            print('Title: ' + entry['dc:title'])
            print('Citation Count: ' + entry['citedby-count'])
            print('\n')


    return str(data)


