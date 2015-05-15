from django.shortcuts import render
from django.http import HttpResponse
import os
import shutil
import json
import requests
import xmltodict
import xml.etree.ElementTree as ET

from .Sources.IEEEXplorer import getIEEEData
from .Sources.PLOS import getPLOSData
from .Sources.BioMed import getBioMedData
from .Sources.arvix import getArvixData
from .Sources.Scopus import get_scopus_info

# SCOPUS API KEY: 19b4b3546222699157deac547bc8e232

# Create your views here.

'''
Function Based View

__author__ = Vishrut Reddi
'''

'''
Request Will be made from urls.py.

@param request
'''

def home(request):

	
	print("Paper Name: " + request.POST.get("paper_name", ""))
	print("Author(s): " + request.POST.get("authors", ""))
	print("University: " + request.POST.get("affiliation", ""))


	author_name = "" + request.POST.get("paper_name", "")
	paper_name = "" + request.POST.get("authors", "")
	affiliation = "" + request.POST.get("affiliation", "")

	# Refreshing the file, Clearing the old data
	shutil.copy2('RIDashboard/templates/result_template.html', 'RIDashboard/templates/result.html')


	with open('RIDashboard/templates/result.html', 'a') as result_file:
	

		data = ""

		gs_data =""
		biomed_data = ""
		scopus_data = ""

		# Get IEEE-Xplorer Data
		ieeeData = getIEEEData(str(request.POST.get("authors", "")), str(request.POST.get("affiliation", "")))

		if ieeeData != 'No Result Possible. Invalid Inputs or no results produced from IEEE Explorer.':
			data += "<div style=\"margin-left: 10px\"><h1><u><span class=\"glyphicon glyphicon-education\" aria-hidden=\"true\"> IEEE-Explorer </u></h1><br></div>"
			data += '<table class="table table-hover">'
			data += '<thead>'
			data += '<tr>'
			data += '<th>Row</th>'
			data += '<th>Title</th>'
			data += '<th>Authors</th>'
			data += '<th>Affiliation(s)</th>'
			data += '<th>Publication-Title</th>'
			data += '<th>Publication-Year</th>'
			data += '<th>Pages(s)</th>'
			data += '<th>ISBN</th>'
			data += '<th>PDF Link</th>'
			data += '</tr>'
			data += '</thead>'
			data += '<tbody>'

			print(len(ieeeData['title']))
			print(len(ieeeData['authors']))
			print(len(ieeeData['affiliations']))
			print(len(ieeeData['pubtitle']))
			print(len(ieeeData['py']))
			print(len(ieeeData['spage']))
			print(len(ieeeData['epage']))
			print(len(ieeeData['isbn']))
			print(len(ieeeData['pdf']))
		

			for i in range(0, len(ieeeData['title'])): 
				data += '<tr id="IEEEXplorer' + str(i) + '" style="cursor: pointer" type="button" data-toggle="modal" data-target="#ieeeModal' + str(i) + '">'
				data += '<td>' + str(i + 1) + '</td>'
				data += '<td>' + ieeeData['title'][i] + '</td>'
				data += '<td>' + ieeeData['authors'][i] + '</td>'
				data += '<td>' + ieeeData['affiliations'][i] + '</td>'
				data += '<td>' + ieeeData['pubtitle'][i] + '</td>'
				data += '<td>' + ieeeData['py'][i] + '</td>'
				data += '<td>' + ieeeData['spage'][i] + ' - ' + ieeeData['epage'][i] + '</td>'
				data += '<td>' + ieeeData['isbn'][i] + '</td>'
				data += '<td>' + ieeeData['pdf'][i] + '</td>'
				data += '</tr>'
				data += '<!-- IEEE - Modal - ' + str(i) + ' -->'
				data += '<div class="modal fade" id="ieeeModal' + str(i) +'" tabindex=\"-1\" role=\"dialog\" aria-labelledby=\"myModalLabel\" aria-hidden=\"true\">'
				data += '<div class="modal-dialog">'
				data += '<div class="modal-content">'
				data += '<div class="modal-header">'
				data += '<h4 class="modal-title" id="myModalLabel">Abstract</h4>'
				data += '</div>'
				data += '<div class="modal-body">'
				data += ieeeData['abstract'][i]
				data += '</div>'
				data += '<div class="modal-footer">'
				data += '<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>'
				data += '</div>'
				data += '</div>'
				data += '</div>'
				data += '</div>'

			data += '</tbody>'
			data += '</table>'

			data += "<hr>"

			data += "<br><br>"


		# Get IEEE-Xplorer Data
		plosData = getPLOSData(str(request.POST.get("authors", "")), str(request.POST.get("affiliation", "")))

		if plosData != 'No Result Possible. Invalid Inputs or no results produced from PLOS.':
			print(len(plosData['title']))
			print(len(plosData['authors']))
			print(len(plosData['abstract']))
			print(len(plosData['plosScore']))
			print(len(plosData['py']))
			print(len(plosData['articleType']))

			data += "<div style=\"margin-left: 10px\"><h1><u><span class=\"glyphicon glyphicon-education\" aria-hidden=\"true\"> PLOS </u></h1><br></div>"
			data += '<table class="table table-hover">'
			data += '<thead>'
			data += '<tr>'
			data += '<th>Row</th>'
			data += '<th>Title</th>'
			data += '<th>Authors</th>'
			data += '<th>Article-Type</th>'
			data += '<th>Publication-Year</th>'
			data += '<th>PLOS Score</th>'
			data += '</tr>'
			data += '</thead>'
			data += '<tbody>'
		

			for i in range(0, len(plosData['title'])): 
				print(str(i))
				data += '<tr id="PLOS' + str(i) + '" style="cursor: pointer;" type="button" data-toggle="modal" data-target="#plosModal' + str(i) + '">'
				data += '<td>' + str(i + 1) + '</td>'
				data += '<td>' + plosData['title'][i] + '</td>'
				data += '<td>' + plosData['authors'][i] + '</td>'
				data += '<td>' + plosData['articleType'][i] + '</td>'
				data += '<td>' + plosData['py'][i] + '</td>'
				data += '<td>' + plosData['plosScore'][i] + '</td>'
				data += '</tr>'
				data += '<!-- PLOS - Modal - ' + str(i) + ' -->'
				data += '<div class="modal fade" id="plosModal' + str(i) +'" tabindex=\"-1\" role=\"dialog\" aria-labelledby=\"myModalLabel\" aria-hidden=\"true\">'
				data += '<div class="modal-dialog">'
				data += '<div class="modal-content">'
				data += '<div class="modal-header">'
				data += '<h4 class="modal-title" id="myModalLabel">Abstract</h4>'
				data += '</div>'
				data += '<div class="modal-body">'
				if plosData['abstract'][i] is None:
					data += '-EMPTY- <br> Data Unavailable at this time.'
				else:
					data += plosData['abstract'][i]
				data += '</div>'
				data += '<div class="modal-footer">'
				data += '<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>'
				data += '</div>'
				data += '</div>'
				data += '</div>'
				data += '</div>'

			data += '</tbody>'
			data += '</table>'

			data += "<br><br>"
			data += "<hr>"

		# Get Google Scholar Data
		# gs_data = getGoogleScholarData(str(request.POST.get("paper_name", "")), str(request.POST.get("authors", "")))
		# gsData += gs_data

		# Get BioMed Data 
		bioMedData = getBioMedData(str(request.POST.get("authors", "")), str(request.POST.get("affiliation", "")))

		if bioMedData != 'No Result Possible. Invalid Inputs or no results produced from BioMed.':
			print(len(bioMedData['title']))
			print(len(bioMedData['authors']))
			print(len(bioMedData['abstractPath']))
			print(len(bioMedData['py']))
			print(len(bioMedData['articleType']))

			data += "<div style=\"margin-left: 10px\"><h1><u><span class=\"glyphicon glyphicon-education\" aria-hidden=\"true\"> Bio-Med </u></h1><br></div>"
			data += '<table class="table table-hover">'
			data += '<thead>'
			data += '<tr>'
			data += '<th>Row</th>'
			data += '<th>Title</th>'
			data += '<th>Authors</th>'
			data += '<th>Article-Type</th>'
			data += '<th>Publication-Year</th>'
			data += '<th>Abstract-Path</th>'
			data += '</tr>'
			data += '</thead>'
			data += '<tbody>'
		

			for i in range(0, len(bioMedData['title'])): 
				print(str(i))
				data += '<tr id="BioMed ' + str(i) + '">'
				data += '<td>' + str(i + 1) + '</td>'
				data += '<td>' + bioMedData['title'][i] + '</td>'
				data += '<td>' + bioMedData['authors'][i] + '</td>'
				data += '<td>' + bioMedData['articleType'][i] + '</td>'
				data += '<td>' + bioMedData['py'][i] + '</td>'
				data += '<td>' + bioMedData['abstractPath'][i] + '</td>'
				data += '</tr>'

			data += '</tbody>'
			data += '</table>'

			data += "<br><br>"
			data += "<hr>"


		# Get Arvix Data 
		arvixData = getArvixData(str(request.POST.get("authors", "")), str(request.POST.get("affiliation", "")))

		if arvixData != 'No Result Possible. Invalid Inputs or no results produced from Arvix.':
			print(len(arvixData['title']))
			print(len(arvixData['authors']))
			print(len(arvixData['abstract']))
			print(len(arvixData['py']))
			print(len(arvixData['affiliations']))

			data += "<div style=\"margin-left: 10px\"><h1><u><span class=\"glyphicon glyphicon-education\" aria-hidden=\"true\"> Arvix </u></h1><br></div>"
			data += '<table class="table table-hover">'
			data += '<thead>'
			data += '<tr>'
			data += '<th>Row</th>'
			data += '<th>Title</th>'
			data += '<th>Author(s)</th>'
			data += '<th>Affiliation(s)</th>'
			data += '<th>Publication-Year</th>'
			data += '</tr>'
			data += '</thead>'
			data += '<tbody>'
		

			for i in range(0, len(arvixData['title'])): 
				print(str(i))
				data += '<tr id="Arvix ' + str(i) + '" style="cursor: pointer;" type="button" data-toggle="modal" data-target="#arvixModal' + str(i) + '">'
				data += '<td>' + str(i + 1) + '</td>'
				data += '<td>' + arvixData['title'][i] + '</td>'
				data += '<td>' + arvixData['authors'][i] + '</td>'
				data += '<td>' + arvixData['affiliations'][i] + '</td>'
				data += '<td>' + arvixData['py'][i] + '</td>'
				data += '</tr>'

				data += '<!-- Arvix - Modal - ' + str(i) + ' -->'
				data += '<div class="modal fade" id="arvixModal' + str(i) +'" tabindex=\"-1\" role=\"dialog\" aria-labelledby=\"myModalLabel\" aria-hidden=\"true\">'
				data += '<div class="modal-dialog">'
				data += '<div class="modal-content">'
				data += '<div class="modal-header">'
				data += '<h4 class="modal-title" id="myModalLabel">Abstract</h4>'
				data += '</div>'
				data += '<div class="modal-body">'
				if arvixData['abstract'][i] is None:
					data += '-EMPTY- <br> Data Unavailable at this time.'
				else:
					data += arvixData['abstract'][i]
				data += '</div>'
				data += '<div class="modal-footer">'
				data += '<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>'
				data += '</div>'
				data += '</div>'
				data += '</div>'
				data += '</div>'

			data += '</tbody>'
			data += '</table>'

			data += "<br><br>"
			data += "<hr>"

		# data += "<br><br>"

		# Get Scopus Data 
		# SCOPUS_API_KEY = ''
		# scopus_data = getScopusData(str(request.POST.get("paper_name", "")), author_name, affiliation)
		# data += str(scopus_data)

		data += '</body></html>'

		result_file.write(data)
		result_file.close()

		if(len(data) >= 300):
			context = {}
			template = "result.html"
			return render(request, template, context)

	context = {}
	template = "home.html"
	return render(request, template, context)


def getScopusData(paper_name, author_name, affiliation):

	scopus_data = "<div class=\"container\"><h1><u><span class=\"glyphicon glyphicon-education\" aria-hidden=\"true\"> SCOPUS </u></h1><br></div>"

	scopus_data += get_scopus_info(paper_name)

	# if(len(paper_name) == 0):
	# 	scopus_data += get_scopus_info(author_name)


	# Need a method here to convert search query into SCOPUS ID(s) 

	# scopus_data += get_scopus_info(API_KEY, 'SCOPUS_ID:0037368024')
	# scopus_data += get_scopus_info(API_KEY, 'SCOPUS_ID:84898934670')
	# scopus_data += get_scopus_info(API_KEY, 'SCOPUS_ID:84872864754')
	# scopus_data += get_scopus_info(API_KEY, 'SCOPUS_ID:84876703352')
	# scopus_data += get_scopus_info(API_KEY, 'SCOPUS_ID:80051860134')
	# scopus_data += get_scopus_info(API_KEY, 'SCOPUS_ID:80051809046')
	# scopus_data += get_scopus_info(API_KEY, 'SCOPUS_ID:79953651013')


	# MORE SAMPLE SCOPUS IDs for Testing
	#================================#
		# SCOPUS_ID:79953651013
		# SCOPUS_ID:79952860396
		# SCOPUS_ID:79951537083
		# SCOPUS_ID:79251517782
		# SCOPUS_ID:77956568341
		# SCOPUS_ID:77954747189
		# SCOPUS_ID:77956693843
		# SCOPUS_ID:77949916234
		# SCOPUS_ID:77955464573
		# SCOPUS_ID:72049114200
		# SCOPUS_ID:78649528829
		# SCOPUS_ID:78649504144
		# SCOPUS_ID:77952266872
		# SCOPUS_ID:73149124752
		# SCOPUS_ID:73149109096
	#================================#


	return scopus_data



def getGoogleScholarData(paper_name, author_name):

	# GS Data stored in String
	# HTML Formatted
	gs_data = "<div class=\"container\"><h1><u><span class=\"glyphicon glyphicon-education\" aria-hidden=\"true\"> Google Scholar </u></h1><br></div>"


	gs_data += "<table><td>"

	line = ""

	for char in os.popen("python3 scholar.py -c 3 --author \"" + author_name + "\" --phrase \"" + paper_name + "\"").read():
		if (char == "\n"):
			first_word = ""

			# Remove White-Spaces from the Ends
			line = line.strip()
			line = line.replace(" ", "-")
			gs_data += line 
			line = ""
			char = "<br>"

		line += char

	gs_data += "</td></table>"
	return gs_data




