from django.shortcuts import render
from django.http import HttpResponseRedirect
#from django.template import RequestContext
from main.models import Email, Beer, Language, Shirt, Thanks
from main.forms import EmailForm, BeerForm, LanguageForm, ShirtForm


def home(request):
    return render(request, 'main/index.html', {})


def email_form(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks-for-your-input/4')
    else:
        form = EmailForm()
    return render(request, 'main/email_form.html', {'form': form})


def beer_form(request):
    if request.method == 'POST':
        form = BeerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks-for-your-input/5')
    else:
        form = BeerForm()
    return render(request, 'main/beer_form.html', {'form': form})


def language_form(request):
    if request.method == 'POST':
        form = LanguageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks-for-your-input/02')
    else:
        form = LanguageForm()
    return render(request, 'main/language_form.html', {'form': form})


def shirt_form(request):
    if request.method == 'POST':
        form = ShirtForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks-for-your-input/03')
    else:
        form = ShirtForm()
    return render(request, 'main/shirt_form.html', {'form': form})


def all_emails(request):
    return render(request, 'main/all_emails.html', {'emails': Email.objects.all()})


def campaigns(request):
    return render(request, 'main/campaigns.html')


def thanks(request, thanks_id):
    return render(request, 'main/thanks.html', {'thanks': Thanks.objects.get(id=int(thanks_id))})
	
def about(request):
    return render(request, 'main/about.html')