from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render, redirect
from .models import Entry
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
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
    if request.method == 'POST':
        form = forms.WriteEntry(request.POST, request.FILES)
        if form.is_valid():
            #save article to db
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect('entries:list')
    else:
        form = forms.WriteEntry()
    return render(request, "entry_write.html", {'form': form})

    
def like_entry (request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    entry.likes += 1
    entry.save()
    return redirect('entry_detail', pk=entry_id)
