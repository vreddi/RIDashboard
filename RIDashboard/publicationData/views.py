from django.shortcuts import render
from django.http import HttpResponse
import os

from .Sources.IEEEXplorer import queryCreator

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

	data = ""
	ieee_data = ""
	data += "<h2> Google Scholar: </h2><br><br>"

	for line in os.popen("python3 scholar.py -c 5 --author \"" + request.POST.get("authors", "") + "\" --phrase \"" + request.POST.get("paper_name", "") + "\"").read():
		if (line == "\n"):
			line = "<br>"
		data += line

	data += "<br><br>"
	data += "<h2> IEEE Xplorer: </h2><br><br>"
	ieee_data += queryCreator(request.POST.get("paper_name", ""), request.POST.get("authors", ""), request.POST.get("affiliation", ""))


	if(len(ieee_data) > 10):
		data += ieee_data
		return HttpResponse(data)

	context = {}
	template = "home.html"
	return render(request, template, context)