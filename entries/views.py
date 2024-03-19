from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render, redirect, reverse
from .models import Entry, Comment
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from .forms import CommentForm

# Create your views here.


def entry_list(request):
    entries = Entry.objects.all().order_by('created_on')
    return render(request, 'entry_list_template.html', {'entries': entries})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comment_set.all() # assuming Comment has a ForeignKey to Post
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
    else:
        form = CommentForm()
    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'form': form})




@login_required(login_url="/accounts/login")
def entry_detail(request, slug):
    entry = get_object_or_404(Entry, slug=slug)
    return render(request, 'entry_detail.html', {'entry': entry})

    entry = Entry.objects.get(slug=slug)

    if request.method == 'POST':
        form = forms.WriteComment(request.POST, request.FILES)
        if form.is_valid():
            # TO DO!!!! stole this from the write entry stuff. need to make it work for comments!
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect('entries:list') # need to change to just refresh
    else:
        form = forms.WriteComment()

    return render(request, 'entry_detail.html', {'entry': entry, 'form': form})

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

    


def like_entry(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    entry.likes += 1
    entry.save()
    # Redirect to the entry detail page after liking
    return redirect('entries_app:detail', slug=entry.slug)
    
