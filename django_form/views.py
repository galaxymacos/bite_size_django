from django.http import HttpResponseRedirect
from django.shortcuts import render

from django_form.forms import NameForm


# Create your views here.
def get_name(request):

    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            your_name = form.cleaned_data["your_name"]
            return HttpResponseRedirect('/django_form/thanks')
    else:
        form = NameForm()
    return render(request, 'name.html', {"form": form})


def thanks(request):
    return render(request, 'thanks.html')
