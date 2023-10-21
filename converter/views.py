from django.shortcuts import render
from django.views import View
from .forms import EditorForm

# Create your views here.

def index(request):
	form = EditorForm()
	return render(request, 'converter/index.html', {'form': form})