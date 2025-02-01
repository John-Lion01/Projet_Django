# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import ReponseForm

def Questionnaire_view(request):
    if request.method == "POST":
        form = ReponseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = ReponseForm()
    
    return render(request, "Questionnaire/formulaire.html", {"form": form})

def success_view(request):
    return render(request, "Questionnaire/success.html")


def homepage(request):
    return redirect('Questionnaire')