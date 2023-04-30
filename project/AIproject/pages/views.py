from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import SearchForm
from django.views.decorators.csrf import csrf_exempt
from .functions import *
# Create your views here.

@csrf_exempt
def homepage(request):
    template_name = 'home.html'
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['main_search']
            url = create_url(query)
            df = results_provenance(url)
            table_html = df.to_html()
            return render(request, template_name, {'form': form, 'query': query, 'table_html': table_html})
                   
        else:
            return render(request, template_name, {'form': form})

    else:
        form = SearchForm()
    
    return render(request,template_name,{'form':form})