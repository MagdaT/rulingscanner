from django import forms
from rulingscanner import models
from simple_search import search_form_factory


from rulingscanner.models import Tag, Authors, TaxType, Ruling

OUTCOME = [
    ('Wszystkie', "Wszystkie"),
    ('Interpretacja pozytywna', 'Interpretacja pozytywna'),
    ('Interpretacja negatywna', 'Interpretacja negatywna'),
]


# SearchForm = search_form_factory(Ruling.objects.all(),
#                                  ['content', 'ruling_no'])

class SearchRulingForm(forms.Form):
    content = forms.CharField(required=False,label="Szukane słowa", max_length=600)
    start_date = forms.DateField(required=False, label="Data wydania OD", input_formats='%Y,%m,%d', widget=forms.SelectDateWidget())
    end_date = forms.DateField(required=False, label="Data wydania OD", input_formats='%Y,%m,%d', widget=forms.SelectDateWidget())
    tag = forms.ModelMultipleChoiceField(required=False, label="Słowa kluczowe", queryset=Tag.objects.all().order_by("name"))
    type_of_tax = forms.ModelChoiceField (required=False, label="Rodzaj podatku", queryset=TaxType.objects.all().order_by("name"))
    author=forms.ModelChoiceField(required=False, label="Organ wydający", queryset=Authors.objects.all().order_by("name"))
    outcome=forms.ChoiceField(required=False, label="Ocena stanowiska podatnika", choices=OUTCOME )
    ruling_no=forms.CharField(required=False, label="Sygnatura", max_length=100)

class AddCommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 1, 'cols': 80}),
        max_length=models.MAXIMUM_COMMENT_LENGTH,
        label='')

    class Meta:
        model = models.Comment
        fields = ['content']
        labels = False

