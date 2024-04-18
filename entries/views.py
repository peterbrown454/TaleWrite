from django.shortcuts import get_object_or_404, redirect, render, reverse
from .models import Entry, Comment
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from . import forms
from .forms import CommentForm, UpdateEntry, WriteEntry
from django.views import generic
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from entries.models import Genre




class two (ListView):
    model = Entry
    template_name = "two.html"
    queryset=Entry.objects.all()
    context_object_name = "entries"           

class search_bar(ListView):
    model = Entry
    template_name = 'entry_list_search.html'
    context_object_name = "entries"

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Entry.objects.filter(title).order_by('created_on')


# def entry_list_genre(request):
    
#     genre_type = '4'  
#     entries = Entry.objects.filter(genre=genre_type)  
#     return render(request, 'entry_list_genre.html', {'entries': entries})

# class GenreListView(ListView):
#     model = Genre
#     template_name = "genre_list.html"

def entry_list_search(request):
    entries = Entry.objects.filter(status=1).order_by('-created_on')
    return render(request, 'entry_list_search.html', {'entries': entries})


# def entry_list(request):
#     entries = Entry.objects.filter(status=1).order_by('-created_on')
#     return render(request, 'entry_list.html', {'entries': entries})


@login_required(login_url="/accounts/login")
def entry_list_draft(request):
    user = request.user
    entries = Entry.objects.filter(author=user).order_by('-created_on')
    return render(request, 'entry_list_draft.html', {'entries': entries})




class EntryListView(ListView):
    model = Entry
    status = 1
    template_name = "entry_list.html"
    context_object_name = "entries"

class search_bar(EntryListView):
    model = Entry
    status = 1
    template_name = "entry_list.html"
    context_object_name = "entries"

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Entry.objects.filter(title=query, genre=query, author=query).order_by('-created_on')




@login_required(login_url="/accounts/login")
def entry_detail(request, slug):
    entry = get_object_or_404(Entry, slug=slug)
    comments = entry.comments.all().order_by("-created_on")
    comment_count = entry.comments.filter(approved=True).count() 

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

# WORKING MODEL
# @login_required(login_url="/accounts/login")
# def entry_write(request):
#     if request.method == 'POST':
#         form = forms.WriteEntry(request.POST, request.FILES)
#         if form.is_valid():
#             title = form.cleaned_data['title']
#             if Entry.objects.filter(title=title).exists():
#                 messages.error(request, "A tale with the same title already exists. Please choose a different title.")
#             else:
#                 instance = form.save(commit=False)
#                 instance.author = request.user
#                 instance.save()
#                 messages.success(request, "Tale successfully published")
#                 return redirect('entries:list')
#     else:
#         form = forms.WriteEntry()
#     return render(request, "entry_write.html", {'form': form})



@login_required(login_url="/accounts/login")
def entry_write(request):
    if request.method == 'POST':
        form = forms.WriteEntry(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            if Entry.objects.filter(title=title).exists():
                messages.error(request, "A tale with the same title already exists. Please choose a different title.")
            else:
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save()
                if instance.status == 0:
                    messages.success(request, "Draft successfully saved to 'My Page'")
                elif instance.status == 1:
                    messages.success(request, "Tale successfully published")
                return redirect('entries:list')
    else:
        form = forms.WriteEntry()
    return render(request, "entry_write.html", {'form': form})



def like_entry(request, slug):
    entry = get_object_or_404(Entry, slug=slug)
    if request.user == entry.author:
        return redirect('entries:entry_detail', slug=entry.slug)
    entry.likes += 1
    entry.save()
    return redirect('entries:entry_detail', slug=entry.slug)



def delete_entry(request, slug):
    entry = get_object_or_404(Entry, slug=slug)
    if request.user == entry.author:
        entry.delete()
        messages.success(request, "Tale successfully deleted")
        return redirect(reverse('entries:list'))
    else:
        messages.error(request, "You don't have permission to delete this entry")
    return redirect(reverse('entries:list'))



 
class EditEntry(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Entry
    form_class = WriteEntry
    template_name = 'entry_edit.html'
    success_url = reverse_lazy('entries:list')
    success_message = "Tale successfully edited"

    def form_valid(self, form):  
        self.model.created_on = timezone.now()
        return super().form_valid(form)
    




   

   
