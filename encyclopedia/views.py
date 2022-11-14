from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def newPage(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title=title, content=content)

    return render(request, "encyclopedia/newPage.html")

def entry(request, title):
    post = util.get_entry(title=title)
    context = {
        'post': post
    }
    return render (request, "encyclopedia/entry.html", context)