from django.shortcuts import render

def index(request):
    return render(request, 'bookmodules/index.html')

def html5_links(request):
    return render(request, 'bookmodules/html5_links.html')

def text_formatting(request):
    return render(request, 'bookmodules/text_formatting.html')

def listing(request):
    return render(request, 'bookmodules/listing.html')

def tables(request):
    return render(request, 'bookmodules/tables.html')
