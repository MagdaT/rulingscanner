from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
# from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.
from django.template.response import TemplateResponse

from rulingscanner.forms import SearchRulingForm
from rulingscanner.models import *
from django.views import View
from rulingscanner import forms


def main_page(request):
    rulings = Ruling.objects.all().order_by( '-creation_date' )
    important_ruling = Ruling.objects.get( important_ruling=True )
    paginator = Paginator( rulings, 1 )
    page = request.GET.get( 'page' )
    ruling_list = paginator.get_page( page )
    ctx = {
        "rulings": ruling_list,
        "important_ruling": important_ruling
    }
    return TemplateResponse( request, 'main.html', context=ctx )


def like_post(request):
    hint = get_object_or_404( Ruling, id=request.POST.get( "hint.id" ) )
    hint.important_by_user.add( request.user )
    return HttpResponseRedirect( "like-post" )


class RulingDetailView(View ):

    def get(self, request, pk):
        ruling = Ruling.objects.get( pk=pk )
        add_comment = forms.AddCommentForm()

        # ctx = {
        #     "ruling": ruling,
        #     "ruling.content": ruling.content,
        #     "ruling.creation_date": ruling.creation_date,
        #     "ruling.tags": ruling.tags,
        #     "ruling.ruling_no": ruling.ruling_no,
        #     "ruling.author": ruling.author,
        #     'add_comment': add_comment
        # }
        return render( request, 'ruling_details.html',
                       {'ruling': ruling, 'add_comment': add_comment} )

    def post(self, request, pk):
        form = forms.AddCommentForm( request.POST )
        ruling = Ruling.objects.get( pk=pk )
        if form.is_valid():
            content = form.cleaned_data.get( 'content' )
            new_comment = Comment(
                content=content, author=request.user, ruling=ruling )
            new_comment.save()
            form = forms.AddCommentForm()
        return render( request, 'ruling_details.html',
                       {'ruling': ruling, 'add_comment': form} )


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm( request.POST )
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get( 'username' )
            raw_password = form.cleaned_data.get( 'password1' )
            user = authenticate( username=username, password=raw_password )
            login( request, user )
            return redirect( 'rulingscanner:main-page' )
    else:
        form = UserCreationForm()

    return render( request, 'register.html', {'form': form} )


def trends(request):
    pass


class SearchRulingView(View):
    def get (self,request):
        form = SearchRulingForm()
        ctx = {"form":form}
        return render(request, "search.html", ctx)
    def post (self, request):
        form = SearchRulingForm(request.POST)
        if form.is_valid():
            result=Ruling.objects.all()
            start_date=form.cleaned_data.get( 'start_date')
            end_date=form.cleaned_data.get( 'end_date')
            tag=form.cleaned_data.get('tag')
            tax_type=form.cleaned_data.get( 'type_of_tax')
            author=form.cleaned_data.get( 'author')
            outcome=form.cleaned_data.get( 'outcome')
            ruling_no=form.cleaned_data.get( 'ruling_no')
            phrase = form.cleaned_data.get( 'content')
            if phrase is not None:
                result = Ruling.objects.filter(content__icontains=phrase)
            # if end_date is not None and start_date is not None:
            #     result = result.objects.filter(creation_date__range=[start_date, end_date])
            # if tag is not None:
            #     result = Ruling.objects.filter(tags=tag)
            empty_form = SearchRulingForm() #pusty form bo wpisalismy ()
            ctx={
                "result":result,
                "form": empty_form,
            }
            return render(request, "search.html", ctx)


# class SearchRulingView(View):
#     def get (self,request):
#         form = SearchRulingForm()
#         ctx = {"form":form}
#         return render(request, "search.html", ctx)
#     def post (self, request):
#         form = SearchRulingForm(request.POST)
#         if form.is_valid():
#             phrase = form.cleaned_data.get( 'content')
#             result = Ruling.objects.filter(content__icontains=phrase) #wchodzisz w interakcje z baza danych tutaj, szukasz w tabeli student nazwiska name
#             #icontains - szyka czesciowego matchu ignorujac caps lock
#             empty_form = SearchRulingForm() #pusty form bo wpisalismy ()
#             ctx={
#                 "result":result,
#                 "form": empty_form,
#             }
#             return render(request, "search.html", ctx)

# class SearchRulingForm(forms.Form):
#     content = forms.CharField(required=False,label="Szukane słowa", max_length=600)
#     start_date = forms.DateField(required=False, label="Data wydania OD", input_formats='%Y,%m,%d', widget=forms.SelectDateWidget())
#     end_date = forms.DateField(required=False, label="Data wydania OD", input_formats='%Y,%m,%d', widget=forms.SelectDateWidget())
#     tag = forms.ModelMultipleChoiceField(required=False, label="Słowa kluczowe", queryset=Tag.objects.all().order_by("name"))
#     type_of_tax = forms.ModelChoiceField (required=False, label="Rodzaj podatku", queryset=TaxType.objects.all().order_by("name"))
#     author=forms.ModelChoiceField(required=False, label="Organ wydający", queryset=Authors.objects.all().order_by("name"))
#     outcome=forms.ChoiceField(required=False, label="Ocena stanowiska podatnika", choices=OUTCOME )
#     ruling_no=forms.CharField(required=False, label="Sygnatura", max_length=100)

# class SearchRulingView(View):
#     def get (self,request):
#         form = SearchRulingForm()
#         ctx = {"form":form}
#         return render(request, "search.html", ctx)
#     def post (self, request):
#         form = SearchRulingForm(request.POST)
#         if form.is_valid():
#             result=Ruling.objects.all()
#             start_date=form.cleaned_data.get( 'start_date')
#             end_date=form.cleaned_data.get( 'end_date')
#             tag=form.cleaned_data.get('tag')
#             tax_type=form.cleaned_data.get( 'type_of_tax')
#             author=form.cleaned_data.get( 'author')
#             outcome=form.cleaned_data.get( 'outcome')
#             ruling_no=form.cleaned_data.get( 'ruling_no')
#             phrase = form.cleaned_data.get('content')
#             if phrase is not None:
#                 result = Ruling.objects.filter(content__icontains=phrase)
#
#         # else:
#         #     result = Ruling.objects.all().order_by("creation_date")
#
#         empty_form = SearchRulingForm() #pusty form bo wpisalismy ()
#         ctx={
#             "result":result,
#             "form": empty_form,
#         }
#         return render(request, "search.html", ctx)
#



# @render('search.html')
# def search(request):
#     form = SearchForm(request.GET or {})
#     if form.is_valid():
#         result = form.get_queryset()
#     else:
#         result = Ruling.objects.none()
#
#     return {
#         'form': form,
#         'results': result,
#     }


# class SearchRulingView( View ):
#     def get(self, request):
#         form = SearchRulingForm()
#         ctx = {"form": form}
#         return render( request, "search.html", ctx )
#
#     def post(self, request):
#         try:
#             q = request.GET['q']
#             result = Ruling.objects.filter( content_icontains=q )
#             return render_to_response( 'search.html', {'result': result, 'q': q} )
#         except KeyError:
#             return render_to_response( 'search.html' )

    # try:
    #     q = request.GET['q']
    #     posts = BlogPost.objects.filter( title__search=q ) | \
    #             BlogPost.objects.filter( intro__search=q ) | \
    #             BlogPost.objects.filter( content__search=q )
    #     return render_to_response( 'search/results.html', {'posts': posts, 'q': q} )
    # except KeyError:
    #     return render_to_response( 'search/results.html' )


# if 'q' in request.GET and request.GET['q']:
#         q = request.GET['q']
#         tasks_list = task.objects.filter(task_name__contains=q)
#     else:
#         tasks_list = task.objects.all().order_by("task_name")


def last_added(request):
    last_ten_rulings = Ruling.objects.all().order_by( '-creation_date' )[:10]
    return render( request, 'last_added.html',
                   {'rulings': last_ten_rulings} )
