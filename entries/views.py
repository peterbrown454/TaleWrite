from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render, redirect, reverse
from .models import Entry, Comment
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from . import forms
from .forms import CommentForm, UpdateEntry
from django.views import generic
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView

# Create your views here.

"""
#commented out to try our class based entry list view
def entry_list(request):
    entries = Entry.objects.all().order_by('created_on')
    return render(request, 'entry_list_template.html', {'entries': entries})

"""
#from https://www.youtube.com/watch?v=-s7e_Fy6NRU  its class-based alternative to functions

class EntryListView(ListView):
    model = Entry
    template_name = "entry_list_template.html"
    context_object_name = "entries"




@login_required(login_url="/login")
def entry_detail(request, slug):
    entry = get_object_or_404(Entry, slug=slug)
    comments = entry.comments.all().order_by("-created_on")
    comment_count = entry.comments.filter(approved=True).count() 
###
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.entry = entry
            comment.save()
            messages.add_message(
        request, messages.SUCCESS,
        'Comment submitted and awaiting approval'
    )

    comment_form = CommentForm()

    return render(request, 'entry_detail.html', 
{
    "entry": entry,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
    },
)

   # if request.method == 'POST':
    #    form = forms.WriteComment(request.POST, request.FILES)
      #  if form.is_valid():
        #    instance = form.save(commit = False)
         #   instance.author = request.user
          #  instance.save()
          #  return redirect('entries:list') 
  #  else:
     #   form = forms.WriteComment()

   # return render(request, 'entry_detail.html', {'entry': entry, 'form': form})

@login_required(login_url="/login")
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



def entry_update(request):
    return HttpResponse ("update page")
    #model = Entry
   # template_name = entry_detail_edit.html
    #login_url = 
    #success_url = "/"
    #success_message = "Your tale has been edited"

def like_entry(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    entry.likes += 1
    entry.save()
    # Redirect to the entry detail page after liking
    return redirect('entries:entry_detail', slug=entry.slug)


#def delete_entry(request, slug):
    #entry = Entry.objects.get(pk=slug)
   # entry.delete()
    #return redirect ("entries:list")

#def delete_entry(request, pk):
   # entry = get_object_or_404(Entry, pk=pk)
   # if request.method == 'POST':
       # entry.delete()
        #return redirect('list')  

#def destroy (request, entry_id):
    #entry = Entry.objects.get(Entry_id=Entry_id)
    #entry.delete()
    #return redirect('list')
    #return render(request, 'delete_content.html', {'content': content})



def delete_entry(request, slug):
    entry = get_object_or_404(Entry, slug=slug)
    if request.user == entry.author:
        entry.delete()
        messages.success(request, "Entry deleted successfully.")
        return redirect(reverse('entries:list'))
    else:
        messages.error(request, "You don't have permission to delete this entry.")
    return redirect(reverse('entries:list'))

"""
def entry_edit(request, slug):
    entry = get_object_or_404(Entry, slug=slug)
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
    return render(request, "entry_edit.html", {'form': form, 'entry':entry})
"""
#LMS ONE BELOW

def entry_edit(request, slug):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Entry.objects.filter()
        entry = get_object_or_404(queryset, slug=slug)


        if entry.author == request.user:


            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('entry_detail', args=[slug]))