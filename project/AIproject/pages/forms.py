from django import forms

class SearchForm(forms.Form):
    main_search = forms.CharField(label='search-api', max_length=100)