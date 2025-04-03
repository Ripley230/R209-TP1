from django.shortcuts import render, get_object_or_404, redirect
from .forms import LivreForm
from . import models

# Création d'un livre
def ajout(request):
    if request.method == "POST":
        form = LivreForm(request.POST)
        if form.is_valid():
            livre = form.save()
            return render(request, "bibliotheque/affiche.html", {"Livre": livre})
        else:
            return render(request, "bibliotheque/ajout.html", {"form": form})
    else:
        form = LivreForm()
        return render(request, "bibliotheque/ajout.html", {"form": form})

# Lecture d'un livre spécifique
def read(request, id):
    livre = get_object_or_404(models.Livre, pk=id)
    return render(request, "bibliotheque/affiche.html", {"Livre": livre})

# Liste des livres
def liste(request):
    livres = models.Livre.objects.all()
    return render(request, "bibliotheque/liste.html", {"livres": livres})

# Mise à jour d'un livre
def update(request, id):
    livre = get_object_or_404(models.Livre, pk=id)
    if request.method == "POST":
        form = LivreForm(request.POST, instance=livre)
        if form.is_valid():
            form.save()
            return redirect("liste")
    else:
        form = LivreForm(instance=livre)
    return render(request, "bibliotheque/update.html", {"form": form, "id": id})

# Suppression d'un livre
def delete(request, id):
    livre = get_object_or_404(models.Livre, pk=id)
    livre.delete()
    return redirect("liste")
