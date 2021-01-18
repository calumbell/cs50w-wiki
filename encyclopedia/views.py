from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, name):
    entry = util.get_entry(name)

    return render(request, "encyclopedia/entry.html", {
        "name" : name,
        "entry" : entry
    })

def search(request):
    if request.method == "POST":
        query = request.POST["q"]
        entry = util.get_entry(query)
        if entry:
            url = reverse('entry', kwargs={'name': query})
            return HttpResponseRedirect(url)
        else:
            entries = util.list_entries()
            matches = []

            for entry in entries:
                if query.upper() in entry.upper():
                    matches.append(entry)
            return render(request, "encyclopedia/search.html", {
                "entries" : matches
            })
