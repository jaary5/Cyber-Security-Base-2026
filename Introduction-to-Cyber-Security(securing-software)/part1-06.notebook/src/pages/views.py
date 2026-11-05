from django.shortcuts import render

# Create your views here.

def addPageView(request):
	items   = request.session.get('items', [])		# get data for my session
	content = request.POST.get('content')			# retrieve from html
	items.append(content)							# append the retreived val from html
	items = items[-10:]                             # keep the last 10
	request.session['items'] = items  				# update the session with new data

	return render(request, 'pages/index.html', {'items' : items})


def erasePageView(request):
	items = []
	request.session['items'] = items

	return render(request, 'pages/index.html', {'items' : items})


def homePageView(request):
	# use sessions (the data is stored in a database db.sqlite that is then accessed using a cookie)
	items = request.session.get('items', [])

	# shorter way of writing instead of loader
	# render(request, template-path, context-dictionary)
	return render(request, 'pages/index.html', {'items' : items})
