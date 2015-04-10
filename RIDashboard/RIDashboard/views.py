'''

Function Based View

__author__ = Vishrut Reddi


from django.shortcuts import render




Request Will be made from urls.py.

@param request

def home(request):

	context = {}
	template = "home.html"
	return render(request, template, context)
'''