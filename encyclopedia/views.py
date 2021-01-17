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

    if not entry:
        return HttpResponseRedirect(reverse("error"))

    return render(request, "encyclopedia/entry.html", {
        "name" : name,
        "entry" : entry
    })

def error(request):
    return render(request, "encyclopedia/error.html")
