from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Article, TeamMember
from django.core.mail import send_mail

# Cyour views here.

# Create your views here.
def home(request):
    list_articles = Article.objects.all()
    context = {'liste_articles':list_articles}
    return render(request, 'home.html', context)

def detail(request,id_article):
    article = Article.objects.get(id=id_article)
    category = article.category
    article_en_relation = Article.objects.filter(category=category)[:5]
    return render (request, 'detail.html',{'article': article, 'aer':article_en_relation})

def search(request):
    query = request.GET["article"]
    liste_article = Article.objects.filter(title__contains = query)
    return render (request, 'search.html', {"liste_article":liste_article})

def service(request):
    return render(request, 'service.html')

def about(request):
    team_members = TeamMember.objects.all()
    return render(request, 'about.html', {'team_members': team_members})

def gallery(request):
    return render(request, 'gallery.html')


def contact(request):
    if request.method == 'POST':
        nom = request.POST.get("nom")
        prenoms = request.POST.get("prenoms")
        email = request.POST.get("email")
        sujet = request.POST.get("sujet")
        message = request.POST.get("message")
        
        
        subject = f'Message de {nom}'
        body = f"""
        Nom : {nom}
        Prenoms : {prenoms}
        Email : {email}
        Sujet : {sujet}
        Message : {message}
        """
        
        send_mail(subject , body , email , ['mranebaye@gmail.com'])
        
        return redirect(reverse('confirmation') + f'?nom={nom}&email={email}' )
    
     
    return render(request, 'contact.html')
    
    
    
    
        
def confirmation(request: HttpRequest):
    nom = request.GET.get('nom')
    email = request.GET.get('email')
    # Autres informations à récupérer si nécessaire

    context = {'nom': nom, 'email': email}
    return render(request, 'confirmation.html', context)

