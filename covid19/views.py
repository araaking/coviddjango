from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
import requests
import json

import requests

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "5700e548c5msh6fe2f16cd3c674bp1cf10ejsn7fd15515f36d",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()



def helloworld(request):
    mylist = []
    noofresults = int(response['results'])
    for x in range(0, noofresults):
        mylist.append(response['response'][x]['country'])
    if request.method =="POST":
        selectedcountry= request.POST["selectedcountry"]
        for x in range(0, noofresults):
            if selectedcountry==response['response'][x]['country']:
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                deaths = int(total) - int(active) - int(recovered)
                # print(response['response'][x]['cases']['new'])
        context = {'selectedcountry': selectedcountry, 'mylist': mylist, 'new': new, 'active': active, 'critical': critical, 'recovered': recovered, 'deaths': deaths, 'total': total}
        return render(request,'index2.html',context)
    context = {'mylist': mylist}
    return render(request,'index2.html',context)