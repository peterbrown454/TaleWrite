from django.shortcuts import render
from .models import Entry
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


def entry_list(request):
    entries = Entry.objects.all().order_by('created_on')
    return render(request, 'entry_list_template.html', {'entries': entries})

def entry_detail(request, slug):
    #return HttpResponse(slug)

    entry = Entry.objects.get(slug=slug)
    return render(request, 'entry_detail.html', {'entry': entry})

@login_required(login_url="/accounts/login")
def entry_write (request):
    return render(request, "entry_write.html")
