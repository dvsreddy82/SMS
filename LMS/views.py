from django.shortcuts import render
from django.views.generic.list import ListView
from django.utils import timezone
from .models import Language
from .forms import LanguageForm
# Create your views here.

# Create landing page

def index(request):
    return render(request,"template.html")

def LanguageListView(request):
    languages = Language.objects.all()
    context = {
        'languages':languages,
    }
    return render(request, 'language/list.html',context)