from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "blogo/index.html")


def articles(request, numero_article):
    return render(request, f"blogo/articles_{numero_article}.html")
