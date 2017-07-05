import os

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response

from django.utils.html import escape

def hello(request):
    return HttpResponse(escape(repr(request)))
    return HttpResponse("Hello world")

from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/name/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})


def form_page(http_request, template_name='form.html'):
    #print(os.getcwd())
    return render(http_request, template_name, {})

#def form_completed(http_request):
#    firstname = http_request.GET.get('firstname')
#    lastname = http_request.GET.get('lastname')
#    print(f'Uzytkownik podał: firstname - {firstname} i lastname - {lastname}')
#    #print(os.getcwd())
#    return render_to_response('completed.html')

def form_completed(http_request, template_name='completed.html'):
    #firstname = http_request.GET.get('firstname')
    #lastname = http_request.GET.get('lastname')
    firstname = http_request.POST.get('firstname')
    lastname = http_request.POST.get('lastname')
    data = {}
    data['firstname'] = firstname
    data['lastname'] = lastname
    print(f'Uzytkownik podał: firstname - {firstname} i lastname - {lastname}')
    #print(os.getcwd())
    return render(http_request, template_name, data)
