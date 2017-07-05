import os

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response

from django.utils.html import escape

def hello(request):
    return HttpResponse(escape(repr(request)))
    return HttpResponse("Hello world")

def form_page(http_request, template_name='form.html'):
    #print(os.getcwd())
    return render(http_request, template_name, {})

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
