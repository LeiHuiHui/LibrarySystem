# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from Library.models import *
# Create your views here.
app_name = 'Library'

def HomePage(request):
    return render(request, 'Library/HomePage.html')

@csrf_exempt
def Submit(request):
    if not request.POST:
        return HttpResponse('Whoops!')
    try:
        Id = Excel.objects.filter().order_by('Id')[0].Id + 1
    except Exception as e:
        print(e)
        Id = 1
    Excel(
        Id = Id,
        Name = request.POST.get('name'),
        Telephone = request.POST.get('telephone'),
        TimeOne = request.POST.get('TimeOne'),
        TimeTwo = request.POST.get('TimeTwo'),
        TimeThree = request.POST.get('TimeThree'),
        TimeFour = request.POST.get('TimeFour'),
        TimeFive = request.POST.get('TimeFive'),
        TimeSix = request.POST.get('TimeSix'),
        TimeSeven = request.POST.get('TimeSeven'),
        TimeEight = request.POST.get('TimeEight'),
    ).save()
    return HttpResponse('Done!')

def ShowList(request):
    context = {}
    l = Excel.objects.all()
    ll = []
    for i in l:
        item = {}
        item['name'] = i.Name
        item['telephone'] = i.Telephone
        item['TimeOne'] = i.TimeOne
        item['TimeTwo'] = i.TimeTwo
        item['TimeThree'] = i.TimeThree
        item['TimeFour'] = i.TimeFour
        item['TimeFive'] = i.TimeFive
        item['TimeSix'] = i.TimeSix
        item['TimeSeven'] = i.TimeSeven
        item['TimeEight'] = i.TimeEight
        ll.append(item)
    context['ll'] = ll
    return render(request, 'Library/../templates/Library/ListView.html', context)
