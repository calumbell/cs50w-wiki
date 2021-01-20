from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from random import choice
from markdown2 import Markdown

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def edit(request):
    if request.method == "GET":
        return render(request, "encyclopedia/edit.html")

    if request.method == "POST":

        if request.POST["action"] == "edit":
            return render(request, "encyclopedia/edit.html", {
                "name" : request.POST["name"],
                "entry" : util.get_entry(request.POST["name"])
            })

        elif request.POST["action"] == "save":
            util.save_entry(request.POST["name"], request.POST["entry"])
            url = reverse('entry', kwargs={'name': request.POST["name"]})
            return HttpResponseRedirect(url)

def entry(request, name):
    entry = util.get_entry(name)
    markdowner = Markdown()
    return render(request, "encyclopedia/entry.html", {
        "name" : name,
        "entry" : markdowner.convert(entry)
    })

def random(request):
    entries = util.list_entries()
    entry = choice(entries)
    url = reverse('entry', kwargs={'name': entry})
    return HttpResponseRedirect(url)


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
