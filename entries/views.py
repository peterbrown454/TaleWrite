from django.shortcuts import render

# Create your views here.


def entry_list(request):
    return render(request, 'entry_list_template.html')